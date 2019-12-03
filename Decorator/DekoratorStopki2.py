from DekoratorPotwierdzenia import DekoratorPotwierdzenia

class DekoratorStopki2(DekoratorPotwierdzenia):
    def __init__(self, zamowienie):
        super().__init__(zamowienie)

    def drukuj(self):
        super().drukuj()
        self.drkStopka()

    def drkStopka(self):
        print("STOPKA 2")
