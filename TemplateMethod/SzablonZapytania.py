from abc import ABC, abstractmethod

class SzablonZapytania(ABC):
    @abstractmethod
    def formatujSelect(self):
        pass

    def wykonajZapytanie(self, specZapyt):
        print(self.formatujSelect(specZapyt))

