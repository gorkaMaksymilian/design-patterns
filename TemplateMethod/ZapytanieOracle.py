from SzablonZapytania import SzablonZapytania

class ZapytanieOracle(SzablonZapytania):
    def fromatujConnect(self):
        pass

    def formatujSelect(self, specZapyt):
        specZapyt += ';'
        return specZapyt

