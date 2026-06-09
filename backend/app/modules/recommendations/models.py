from pydantic import BaseModel


class FruitRecommendation(BaseModel):
    id: int
    name: str
    category: str
    freshness_score: int
    origin: str
    price: float
    tags: list[str]
    reason: str
