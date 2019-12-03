from ApNadzorujaca import ApNadzorujaca
from Konfiguracja import Konfiguracja

konfiguracja = Konfiguracja('W')
apNadzorujaca = ApNadzorujaca(konfiguracja)
apNadzorujaca.drukuj()
apNadzorujaca.rysuj()

konfiguracja2 = Konfiguracja('N')
apNadzorujaca2 = ApNadzorujaca(konfiguracja2)
apNadzorujaca2.drukuj()
apNadzorujaca2.rysuj()
