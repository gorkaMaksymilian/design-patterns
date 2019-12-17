from abc import ABC, abstractmethod

class Colleague(ABC):
    @abstractmethod
    def changed(self):
        pass

    @abstractmethod
    def set_mediator(self, mediator):
        pass
