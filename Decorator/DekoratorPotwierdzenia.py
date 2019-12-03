from Komponent import Komponent

class DekoratorPotwierdzenia(Komponent):
    def __init__(self, komponent):
        self.mojKomponent = komponent

    def drukuj(self):
        if self.mojKomponent != None:
            self.mojKomponent.drukuj()
        else:
            raise "mojKomponent nie istnieje"

