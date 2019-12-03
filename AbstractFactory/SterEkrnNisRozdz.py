from SterownikEkranu import SterownikEkranu
from SENR import SENR

class SterEkrnNisRozdz(SterownikEkranu):
    def __init__(self):
        self.sterownik = SENR()

    def rysuj(self):
        self.sterownik.rysuj()
