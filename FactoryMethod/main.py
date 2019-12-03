from ZapytanieSQLServer import ZapytanieSQLServer
from ZapytanieOracle import ZapytanieOracle

zapytanie = 'SELECT * from pracownicy'

SQLServer = ZapytanieSQLServer()
SQLServer.wykonajZapytanie(zapytanie)
print()

Oracle = ZapytanieOracle()
Oracle.wykonajZapytanie(zapytanie)
