from BazaDanych import BazaDanych

class BazaDanychOracle(BazaDanych):
    def wykonajZapytanie(self, specZapyt):
        print(specZapyt)

    def __str__(self):
        return "Oracle"

