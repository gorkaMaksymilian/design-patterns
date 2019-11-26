from Zamowienie import Zamowienie
from Konfiguracja import Konfiguracja


moje_zamowienie = Zamowienie('batonik', 'batonik', 'herbata', 'woda')

print('Ceny w niemczech')
moje_zamowienie.obliczPodatek()

moje_zamowienie.konfiguracja = Konfiguracja('PL')
moje_zamowienie.metoda = moje_zamowienie.konfiguracja.zwroc_metode_obliczania()

print('\nCeny w polsce')
moje_zamowienie.obliczPodatek()

