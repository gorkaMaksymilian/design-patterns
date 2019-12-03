from abc import ABC, abstractmethod

class SzablonZapytania(ABC):
    @abstractmethod
    def formatujSelect(self):
        pass

    def wykonajZapytanie(self, specZapyt):
        self.baza = self.utworzBD()
        print(f"przekazuje zaptanie do bazy {self.baza}")
        self.baza.wykonajZapytanie(self.formatujSelect(specZapyt))

    def utworzBD(self):
        pass
