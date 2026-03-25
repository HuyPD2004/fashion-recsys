from domain.models.hybrid_model import HybridModel

class RecommenderService:
    def __init__(self):
        self.model = HybridModel()

    def recommend(self, user_id: str, k: int = 10):
        return self.model.predict(user_id, k)