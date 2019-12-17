from Visitor import Visitor

class WeterynarzVisitor(Visitor):
    def visit(self, zwierze):
        if zwierze.zdrowe == False:
            print(f'Odwiedzam zwierze: {zwierze.nazwa}. Diagnoza: choroba. Leczenie: antybiotyki')
        else:
            print(f'Odwiedzam zwierze: {zwierze.nazwa}. Diagnoza: zdrowe.')

    def visit_ptak(self, ptak):
        if ptak.zdrowe == False:
            if ptak.cena_czarnorynkowa > 2*ptak.cena:
                print(f'Zabieram zwierze: {ptak.nazwa} do lecznicy.')
            else:
                print(f'Odwiedzam zwierze: {ptak.nazwa}. Diagnoza: choroba. Leczenie: antybiotyki, dieta')
        else:
            print(f'Odwiedzam zwierze: {ptak.nazwa}. Diagnoza: zdrowe.')

