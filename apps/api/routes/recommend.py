from fastapi import APIRouter
from application.inference.recommend import recommend_for_user

router = APIRouter(prefix="/recommend", tags=["recommend"])

@router.get("/")
def recommend(user_id: str, k: int = 10):
    results = recommend_for_user(user_id, k)
    return {"user_id": user_id, "recommendations": results}