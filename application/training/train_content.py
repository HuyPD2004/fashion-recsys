from domain.models.content_model import ContentModel

def train_content(data):
    model = ContentModel()
    model.train(data)
    return model