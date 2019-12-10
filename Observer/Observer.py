from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def Update(self):
        pass
