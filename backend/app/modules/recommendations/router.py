from fastapi import APIRouter, Query

from app.modules.recommendations.models import FruitRecommendation
from app.modules.recommendations.service import list_recommendations

router = APIRouter()


@router.get("", response_model=list[FruitRecommendation])
def get_recommendations(
    member_id: int | None = Query(default=None, gt=0),
) -> list[FruitRecommendation]:
    return list_recommendations(member_id)
