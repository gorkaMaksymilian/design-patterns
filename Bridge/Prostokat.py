from Figura import Figura

class Prostokat(Figura):
    def __init__(self, biblioteka):
        self.biblioteka = biblioteka

    def rysuj(self):
        self.rysujLinie()
        self.rysujLinie()
        self.rysujLinie()
        self.rysujLinie()
