from SzablonZapytania import SzablonZapytania
from BazaDanychOracle import BazaDanychOracle

class ZapytanieOracle(SzablonZapytania):
    def fromatujConnect(self):
        pass

    def formatujSelect(self, specZapyt):
        specZapyt += ';'
        return specZapyt

    def utworzBD(self):
        return BazaDanychOracle()
