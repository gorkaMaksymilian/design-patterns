from Figura import Figura

class Okrag(Figura):
    def __init__(self, biblioteka):
        self.biblioteka = biblioteka

    def rysuj(self):
        self.rysujOkrag()
