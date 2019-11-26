from abc import ABC, abstractmethod
from Biblioteka import Biblioteka

class Figura(ABC):
    @abstractmethod
    def rysuj(self):
        pass

    def rysujLinie(self):
        self.biblioteka.rysujLinie()

    def rysujOkrag(self):
        self.biblioteka.rysujOkrag()
