from SterownikEkranu import SterownikEkranu
from SEWR import SEWR

class SterEkrnWysRozdz(SterownikEkranu):
    def __init__(self):
        self.sterownik = SEWR()

    def rysuj(self):
        self.sterownik.rysuj()
