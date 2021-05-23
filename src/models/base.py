from abc import ABC, abstractmethod

class Model(ABC):
  @abstractmethod
  def fit(self, x, y, t) -> 'Model':
    return self

  @abstractmethod
  def predict(self, x):
    pass
