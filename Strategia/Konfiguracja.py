from PodatekPolska import PodatekPolska
from PodatekNiemcy import PodatekNiemcy

class Konfiguracja:
    def __init__(self,kraj):
        self.kraj = kraj

    def zwroc_metode_obliczania(self):
        if self.kraj == 'DE':
            return PodatekNiemcy()
        if self.kraj == 'PL':
            return PodatekPolska()
        else:
            raise 'Brak kraju w bazie'
