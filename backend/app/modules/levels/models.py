from pydantic import BaseModel, Field


class LevelBase(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    min_points: int = Field(ge=0)
    discount: float = Field(gt=0, le=1)
    benefits: list[str] = []


class LevelCreate(LevelBase):
    pass


class Level(LevelBase):
    id: int
