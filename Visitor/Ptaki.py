from Zwierze import Zwierze

class Ptaki(Zwierze):
    def __init__(self, zdrowe, cena, nazwa, cena_czarnorynkowa):
        super().__init__(zdrowe, cena, nazwa)
        self.cena_czarnorynkowa = cena_czarnorynkowa

