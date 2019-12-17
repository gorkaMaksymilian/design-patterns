from Visitor import Visitor

class CzarnorynkowaCenaVisitor(Visitor):
    def __init__(self):
        self.suma = 0

    def visit(self, zwierze):
        self.suma += zwierze.cena

    def visit_ptak(self, ptak):
        self.suma += ptak.cena_czarnorynkowa
