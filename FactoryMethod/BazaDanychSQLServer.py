from BazaDanych import BazaDanych

class BazaDanychSQLServer(BazaDanych):
    def wykonajZapytanie(self, specZapyt):
        print(specZapyt)

    def __str__(self):
        return "SQLServer"
