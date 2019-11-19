from Figura import Figura
from XXOkrag import XXOkrag

class Okrag(Figura):
    def __init__(self):
        self._XXOkrag = XXOkrag()

    def pobierz_polozenie(self):
        self._XXOkrag.pobierz_polozenie()

    def nadaj_polozenie(self):
        self._XXOkrag.nadaj_polozenie()

    def wyswietl(self):
        self._XXOkrag.wyswietlaj()

    def wypelnij(self):
        self._XXOkrag.wypelniaj()

    def nadaj_kolor(self):
        self._XXOkrag.ustaw_kolor()

    def usun(self):
        self._XXOkrag.usuwaj()

