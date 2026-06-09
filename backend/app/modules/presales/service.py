from fastapi import HTTPException

from app.core.store import store
from app.modules.presales.models import Presale, PresaleCreate, PresaleOrder, PresaleOrderCreate


def _presale(data: dict) -> Presale:
    return Presale(**data, remaining=data["quota"] - data["reserved"])


def list_presales() -> list[Presale]:
    return [_presale(presale) for presale in store.presales.values()]


def create_presale(payload: PresaleCreate) -> Presale:
    if payload.end_date < payload.start_date:
        raise HTTPException(status_code=400, detail="结束日期不能早于开始日期")
    presale_id = store.next_id(store.presales)
    presale = {"id": presale_id, **payload.model_dump()}
    store.presales[presale_id] = presale
    return _presale(presale)


def reserve_presale(payload: PresaleOrderCreate) -> PresaleOrder:
    member = store.members.get(payload.member_id)
    presale = store.presales.get(payload.presale_id)
    if not member:
        raise HTTPException(status_code=404, detail="会员不存在")
    if not presale:
        raise HTTPException(status_code=404, detail="预售活动不存在")

    remaining = presale["quota"] - presale["reserved"]
    if payload.quantity > remaining:
        raise HTTPException(status_code=400, detail="预售名额不足")

    presale["reserved"] += payload.quantity
    order = {
        "id": store.next_order_id(),
        "member_id": payload.member_id,
        "presale_id": payload.presale_id,
        "quantity": payload.quantity,
        "amount": round(presale["price"] * payload.quantity, 2),
        "status": "reserved",
    }
    store.presale_orders.append(order)
    return PresaleOrder(**order)
