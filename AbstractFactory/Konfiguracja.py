from FabrykaNisRozdz import FabrykaNisRozdz
from FabrykaWysRozdz import FabrykaWysRozdz

class Konfiguracja:
    def __init__(self, rozdzielczosc):
        self.rozdzielczosc = rozdzielczosc

    def instancjonizuj(self):
        if self.rozdzielczosc == "W":
            return FabrykaWysRozdz()
        elif self.rozdzielczosc == "N":
            return FabrykaNisRozdz()
        else:
            raise "brak fabryki tej rozdzieczosci"


