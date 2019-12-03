from SterownikDrukarki import SterownikDrukarki
from SDNR import SDNR

class SterDrukNisRozdz(SterownikDrukarki):
    def __init__(self):
        self.sterownik = SDNR()

    def drukuj(self):
        self.sterownik.drukuj()
