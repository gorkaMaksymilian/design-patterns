from DekoratorStopki import DekoratorStopki
from DekoratorNaglowka import DekoratorNaglowka
from DekoratorStopki2 import DekoratorStopki2
from DekoratorNaglowka2 import DekoratorNaglowka2
from Potwierdzenie import Potwierdzenie

class Konfiguracja:
    def __init__(self, zamowienie):
        self.zamowienie = zamowienie


    def pobierzPotwierdzenie(self):
        if self.zamowienie == 2:
            return DekoratorNaglowka(DekoratorNaglowka2(DekoratorStopki(Potwierdzenie())))
        elif self.zamowienie == 1:
            return DekoratorNaglowka(DekoratorStopki2(DekoratorStopki(Potwierdzenie())))
        else:
            raise "bledne zamowienie"
