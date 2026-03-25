from domain.models.cf_model import CFModel
from domain.models.content_model import ContentModel

class HybridModel:
    def __init__(self):
        self.cf = CFModel()
        self.cb = ContentModel()

    def predict(self, user_id, k=10):
        cf_items = self.cf.predict(user_id, k)
        cb_items = self.cb.predict(user_id, k)

        # simple merge
        return list(set(cf_items + cb_items))[:k]