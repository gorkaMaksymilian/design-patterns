from HelpHandler import HelpHandler


class ConcreteHandler(HelpHandler):
    def __init__(self, succesor, name):
        self.succesor = succesor
        self.name = name

    def HandleHelp(self):
        if self.succesor == None:
            print(f'{self.name}: potrafie obsluzyc zadanie pomocy')
        else:
            print(f'{self.name}: nie potrafie obsluzyc zadania i przekazuje je dalej')
            self.succesor.ShowHelp()

    def ShowHelp(self):
        print(f'{self.name}: odebralem zadanie wyswietlenia pomocy')
        self.HandleHelp()

