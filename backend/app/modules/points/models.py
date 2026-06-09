from pydantic import BaseModel, Field


class RewardBase(BaseModel):
    title: str = Field(min_length=2, max_length=50)
    points_cost: int = Field(gt=0)
    stock: int = Field(ge=0)
    description: str = ""


class Reward(RewardBase):
    id: int


class RedeemRequest(BaseModel):
    member_id: int = Field(gt=0)
    reward_id: int = Field(gt=0)


class PointAdjustRequest(BaseModel):
    member_id: int = Field(gt=0)
    change: int
    note: str = Field(min_length=2, max_length=80)


class PointRecord(BaseModel):
    id: int
    member_id: int
    change: int
    type: str
    note: str
    created_at: str


class RedeemResult(BaseModel):
    member_id: int
    reward: Reward
    remaining_points: int
    record: PointRecord
