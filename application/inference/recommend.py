from domain.services.recommender import RecommenderService

service = RecommenderService()

def recommend_for_user(user_id: str, k: int = 10):
    return service.recommend(user_id, k)