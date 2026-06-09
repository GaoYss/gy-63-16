from fastapi import APIRouter

from app.modules.levels.router import router as levels_router
from app.modules.members.router import router as members_router
from app.modules.points.router import router as points_router
from app.modules.presales.router import router as presales_router
from app.modules.recommendations.router import router as recommendations_router

api_router = APIRouter()
api_router.include_router(levels_router, prefix="/levels", tags=["levels"])
api_router.include_router(members_router, prefix="/members", tags=["members"])
api_router.include_router(points_router, prefix="/points", tags=["points"])
api_router.include_router(presales_router, prefix="/presales", tags=["presales"])
api_router.include_router(
    recommendations_router, prefix="/recommendations", tags=["recommendations"]
)
