from fastapi import APIRouter

from app.modules.levels.models import Level, LevelCreate
from app.modules.levels.service import create_level, list_levels

router = APIRouter()


@router.get("", response_model=list[Level])
def get_levels() -> list[Level]:
    return list_levels()


@router.post("", response_model=Level, status_code=201)
def post_level(payload: LevelCreate) -> Level:
    return create_level(payload)
