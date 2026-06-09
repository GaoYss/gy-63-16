from datetime import datetime

from fastapi import HTTPException

from app.core.store import store
from app.modules.points.models import PointAdjustRequest, PointRecord, RedeemRequest, RedeemResult, Reward


def list_rewards() -> list[Reward]:
    return [Reward(**reward) for reward in store.rewards.values()]


def list_point_records(member_id: int | None = None) -> list[PointRecord]:
    records = store.point_records
    if member_id is not None:
        records = [record for record in records if record["member_id"] == member_id]
    return [PointRecord(**record) for record in records]


def redeem_reward(payload: RedeemRequest) -> RedeemResult:
    member = store.members.get(payload.member_id)
    reward = store.rewards.get(payload.reward_id)
    if not member:
        raise HTTPException(status_code=404, detail="会员不存在")
    if not reward:
        raise HTTPException(status_code=404, detail="兑换商品不存在")
    if reward["stock"] <= 0:
        raise HTTPException(status_code=400, detail="库存不足")
    if member["points"] < reward["points_cost"]:
        raise HTTPException(status_code=400, detail="会员积分不足")

    member["points"] -= reward["points_cost"]
    reward["stock"] -= 1
    record = {
        "id": store.next_record_id(),
        "member_id": member["id"],
        "change": -reward["points_cost"],
        "type": "redeem",
        "note": f"兑换{reward['title']}",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store.point_records.append(record)

    return RedeemResult(
        member_id=member["id"],
        reward=Reward(**reward),
        remaining_points=member["points"],
        record=PointRecord(**record),
    )


def adjust_points(payload: PointAdjustRequest) -> PointRecord:
    member = store.members.get(payload.member_id)
    if not member:
        raise HTTPException(status_code=404, detail="会员不存在")
    if payload.change == 0:
        raise HTTPException(status_code=400, detail="积分变动不能为0")
    if member["points"] + payload.change < 0:
        raise HTTPException(status_code=400, detail="调整后积分不能小于0")

    member["points"] += payload.change
    record = {
        "id": store.next_record_id(),
        "member_id": member["id"],
        "change": payload.change,
        "type": "earn" if payload.change > 0 else "adjust",
        "note": payload.note,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store.point_records.append(record)
    return PointRecord(**record)
