from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, zwierze):
        pass

    @abstractmethod
    def visit_ptak(self, ptak):
        pass
