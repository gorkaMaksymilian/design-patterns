from FabrykaSter import FabrykaSter
from SterEkrnNisRozdz import SterEkrnNisRozdz
from SterDrukNisRozdz import SterDrukNisRozdz

class FabrykaNisRozdz(FabrykaSter):
    def pobierzSterEkrn(self):
        return SterEkrnNisRozdz()

    def pobierzSterDruk(self):
        return SterDrukNisRozdz()
