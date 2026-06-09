from fastapi import HTTPException

from app.core.store import store
from app.modules.levels.service import get_level
from app.modules.members.models import Member, MemberCreate, MemberUpdate


def _with_level(member: dict) -> Member:
    level = get_level(member["level_id"])
    return Member(**member, level=level)


def list_members() -> list[Member]:
    return [_with_level(member) for member in store.members.values()]


def get_member(member_id: int) -> Member:
    member = store.members.get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="会员不存在")
    return _with_level(member)


def create_member(payload: MemberCreate) -> Member:
    get_level(payload.level_id)
    member_id = store.next_id(store.members)
    member = {"id": member_id, **payload.model_dump()}
    store.members[member_id] = member
    return _with_level(member)


def update_member(member_id: int, payload: MemberUpdate) -> Member:
    existing = store.members.get(member_id)
    if not existing:
        raise HTTPException(status_code=404, detail="会员不存在")

    updates = payload.model_dump(exclude_unset=True)
    if "level_id" in updates:
        get_level(updates["level_id"])
    existing.update(updates)
    return _with_level(existing)
