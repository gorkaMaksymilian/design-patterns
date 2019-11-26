from Konfiguracja import Konfiguracja

class Zamowienie:
    def __init__(self, *towary):
        self.produkty = {'batonik': 2, 'herbata': 13.99, 'woda': 1}
        self.konfiguracja = Konfiguracja('DE')
        self.metoda = self.konfiguracja.zwroc_metode_obliczania()
        self.towary = towary

    def obliczPodatek(self):
        naleznosc = 0
        for towar in self.towary:
            for nazwa, cena in self.produkty.items():
                if towar == nazwa:
                    podatek = self.metoda.kwotaPodatku(cena)
                    print(f'{towar}: {(cena+podatek):.2f}')
                    naleznosc+=cena+podatek
        print(f'suma: {naleznosc:.2f}')
