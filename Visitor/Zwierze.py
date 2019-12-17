from abc import ABC

class Zwierze(ABC):
    def __init__(self, zdrowe, cena, nazwa):
        self.zdrowe = zdrowe
        self.cena = cena
        self.nazwa = nazwa
