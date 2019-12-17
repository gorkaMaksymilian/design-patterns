from Colleague import Colleague

class ConcreteColleague(Colleague):
    def __init__(self, display):
        self.display = display
        self.status = False
        self.mediator = None

    def __str__(self):
        if self.status:
            return f'{self.display}\tX'
        return f'{self.display}'

    def changed(self):
        self.mediator.checkbox_selected(self.display[0])

    def set_mediator(self, mediator):
        self.mediator = mediator


