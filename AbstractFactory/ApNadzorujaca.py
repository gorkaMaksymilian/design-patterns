class ApNadzorujaca:
    def __init__(self, fabryka):
        self.fabryka = fabryka.instancjonizuj()

    def drukuj(self):
        self.fabryka.pobierzSterDruk().drukuj()

    def rysuj(self):
        self.fabryka.pobierzSterEkrn().rysuj()

