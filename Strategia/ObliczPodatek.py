from abc import ABC, abstractmethod

class ObliczPodatek(ABC):
    @abstractmethod
    def kwotaPodatku(self):
        pass

