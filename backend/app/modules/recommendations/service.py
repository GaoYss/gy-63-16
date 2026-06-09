from app.core.store import store
from app.modules.recommendations.models import FruitRecommendation


def list_recommendations(member_id: int | None = None) -> list[FruitRecommendation]:
    favorites: set[str] = set()
    if member_id and member_id in store.members:
        favorites = set(store.members[member_id]["favorite_categories"])

    recommendations = []
    for fruit in store.fruits.values():
        reason = "新鲜度高，适合作为今日主推"
        if fruit["category"] in favorites:
            reason = "匹配会员偏好，建议优先推荐"
        elif fruit["freshness_score"] >= 96:
            reason = "到店批次新鲜度高，可提升复购"
        recommendations.append(FruitRecommendation(**fruit, reason=reason))

    return sorted(
        recommendations,
        key=lambda item: (item.category not in favorites, -item.freshness_score),
    )
