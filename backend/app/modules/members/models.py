from pydantic import BaseModel, Field

from app.modules.levels.models import Level


class MemberBase(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    phone: str = Field(min_length=7, max_length=20)
    level_id: int = Field(gt=0)
    points: int = Field(default=0, ge=0)
    favorite_categories: list[str] = []


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=20)
    phone: str | None = Field(default=None, min_length=7, max_length=20)
    level_id: int | None = Field(default=None, gt=0)
    points: int | None = Field(default=None, ge=0)
    favorite_categories: list[str] | None = None


class Member(MemberBase):
    id: int
    level: Level | None = None
