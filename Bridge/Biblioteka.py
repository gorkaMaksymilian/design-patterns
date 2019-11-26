from abc import ABC, abstractmethod

class Biblioteka(ABC):
    @abstractmethod
    def rysujLinie(self):
        pass

    @abstractmethod
    def rysujOkrag(self):
        pass
