from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def checkbox_selected(self, select):
        pass
