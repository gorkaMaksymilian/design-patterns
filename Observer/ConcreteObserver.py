from Observer import Observer

class ConcreteObserver(Observer):
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.observerState = None
        self.subject.Attach(self)

    def Update(self):
        self.observerState = self.subject.GetState()
        if self.observerState != None:
            print(f'{self.name} wykryl zmiane stanu obserwowanego obiektu')

