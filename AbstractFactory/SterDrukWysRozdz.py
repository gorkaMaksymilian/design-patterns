from SterownikDrukarki import SterownikDrukarki
from SDWR import SDWR

class SterDrukWysRozdz(SterownikDrukarki):
    def __init__(self):
        self.sterownik = SDWR()

    def drukuj(self):
        self.sterownik.drukuj()
