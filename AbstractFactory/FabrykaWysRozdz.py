from FabrykaSter import FabrykaSter
from SterEkrnWysRozdz import SterEkrnWysRozdz
from SterDrukWysRozdz import SterDrukWysRozdz

class FabrykaWysRozdz(FabrykaSter):
    def pobierzSterEkrn(self):
        return SterEkrnWysRozdz()

    def pobierzSterDruk(self):
        return SterDrukWysRozdz()
