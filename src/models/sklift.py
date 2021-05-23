from src.models.base import Model

class SKLiftModel(Model):
  def __init__(self, model):
    self.model = model

  def fit(self, x, y, t) -> Model:
    return self.model.fit(x, y, t)
    
  def predict(self, x):
    return self.model.predict(x)
