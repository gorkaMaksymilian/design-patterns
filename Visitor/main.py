from Gady import Gady
from Ryby import Ryby
from Ssaki import Ssaki
from Ptaki import Ptaki
from OficjalnaCenaVisitor import OficjalnaCenaVisitor
from CzarnorynkowaCenaVisitor import CzarnorynkowaCenaVisitor
from WeterynarzVisitor import WeterynarzVisitor

if __name__ == '__main__':
    zwierzeta = [Ptaki(False, 200, 'papuga', 700), Ptaki(False, 200, 'papuga ara', 300), Ptaki(True, 200, 'golab', 700),
                 Ssaki(False, 150, 'pies'), Ssaki(True, 1500, 'kot'),
                 Ryby(False, 50, 'karp'), Ryby(True, 150, 'sum'),
                 Gady(False, 500, 'waz'), Gady(True, 60, 'jaszczurka')]

    ptaki = zwierzeta[:3]


    print('Zwierzeta w sklepie:')
    for zwierze in zwierzeta:
        print(zwierze.nazwa, end=' ')


    print('\n\nCena oficjalna wszystkich zwierzat w sklepie:')
    cena_oficjalna = OficjalnaCenaVisitor()
    for zwierze in zwierzeta[3:]:
        cena_oficjalna.visit(zwierze)
    for ptak in zwierzeta[:3]:
        cena_oficjalna.visit_ptak(ptak)
    print(cena_oficjalna.suma)

    print('\n\nCena czarnorynkowa wszystkich zwierzat w sklepie:')
    cena_czarnorynkowa = CzarnorynkowaCenaVisitor()
    for zwierze in zwierzeta[3:]:
        cena_czarnorynkowa.visit(zwierze)
    for ptak in zwierzeta[:3]:
        cena_czarnorynkowa.visit_ptak(ptak)
    print(cena_czarnorynkowa.suma)

    print('\n\nWeterynarz:')
    vet = WeterynarzVisitor()
    for zwierze in zwierzeta[3:]:
        vet.visit(zwierze)
    for ptak in zwierzeta[:3]:
        vet.visit_ptak(ptak)
