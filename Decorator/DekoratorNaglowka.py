from DekoratorPotwierdzenia import DekoratorPotwierdzenia

class DekoratorNaglowka(DekoratorPotwierdzenia):
    def __init__(self, zamowienie):
        super().__init__(zamowienie)

    def drukuj(self):
        self.drkNaglowek()
        super().drukuj()

    def drkNaglowek(self):
        print("NAGLOWEK 1")
