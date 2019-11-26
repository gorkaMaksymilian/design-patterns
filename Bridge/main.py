from BibliotekaV1 import BibliotekaV1
from BibliotekaV2 import BibliotekaV2
from Okrag import Okrag
from Prostokat import Prostokat

BG1 = BibliotekaV1()
BG2 = BibliotekaV2()

okrag = Okrag(BG1)
okrag2 = Okrag(BG2)

prostokat = Prostokat(BG1)
prostokat2 = Prostokat(BG2)
print('Rysuje okrag:')
okrag.rysuj()
print('\nRysuje prostokat:')
prostokat.rysuj()

print('\n\nRysuje okrag2:')
okrag2.rysuj()
print('\nRysuje prostokat2:')
prostokat2.rysuj()
