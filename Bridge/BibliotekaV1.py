from Biblioteka import Biblioteka
from BG1 import BG1

class BibliotekaV1(Biblioteka):
    def rysujLinie(self):
        BG1.rysuj_linie()

    def rysujOkrag(self):
        BG1.rysuj_okrag()
