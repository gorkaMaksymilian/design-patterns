from ZapytanieSQLServer import ZapytanieSQLServer
from ZapytanieOracle import ZapytanieOracle

zapytanie = 'SELECT * from pracownicy'
print('SQLServer')
SQLServer = ZapytanieSQLServer()
SQLServer.wykonajZapytanie(zapytanie)

print('\nOracle')
Oracle = ZapytanieOracle()
Oracle.wykonajZapytanie(zapytanie)
