from domain.models.cf_model import CFModel

def train_cf(data):
    model = CFModel()
    model.train(data)
    return model