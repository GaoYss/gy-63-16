from fastapi import APIRouter, Query

from app.modules.points.models import PointAdjustRequest, PointRecord, RedeemRequest, RedeemResult, Reward
from app.modules.points.service import adjust_points, list_point_records, list_rewards, redeem_reward

router = APIRouter()


@router.get("/rewards", response_model=list[Reward])
def get_rewards() -> list[Reward]:
    return list_rewards()


@router.get("/records", response_model=list[PointRecord])
def get_records(member_id: int | None = Query(default=None, gt=0)) -> list[PointRecord]:
    return list_point_records(member_id)


@router.post("/redeem", response_model=RedeemResult)
def post_redeem(payload: RedeemRequest) -> RedeemResult:
    return redeem_reward(payload)


@router.post("/adjust", response_model=PointRecord)
def post_adjust(payload: PointAdjustRequest) -> PointRecord:
    return adjust_points(payload)
