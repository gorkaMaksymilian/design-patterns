from SzablonZapytania import SzablonZapytania
from BazaDanychSQLServer import BazaDanychSQLServer


class ZapytanieSQLServer(SzablonZapytania):
    def formatujConnect(self):
        pass

    def formatujSelect(self, specZapyt):
        return specZapyt

    def utworzBD(self):
        return BazaDanychSQLServer()
