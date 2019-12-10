from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def licz(self, a, b, c):
        pass
