from fastapi import APIRouter

from app.modules.presales.models import Presale, PresaleCreate, PresaleOrder, PresaleOrderCreate
from app.core.store import store
from app.modules.presales.service import create_presale, list_presales, reserve_presale

router = APIRouter()


@router.get("", response_model=list[Presale])
def get_presales() -> list[Presale]:
    return list_presales()


@router.post("", response_model=Presale, status_code=201)
def post_presale(payload: PresaleCreate) -> Presale:
    return create_presale(payload)


@router.post("/orders", response_model=PresaleOrder)
def post_presale_order(payload: PresaleOrderCreate) -> PresaleOrder:
    return reserve_presale(payload)


@router.get("/orders", response_model=list[PresaleOrder])
def get_presale_orders() -> list[PresaleOrder]:
    return [PresaleOrder(**order) for order in store.presale_orders]
