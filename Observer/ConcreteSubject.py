from Subject import Subject

class ConcreteSubject(Subject):
    def __init__(self):
        self.subjectState = False
        self.observers = []

    def Attach(self, observer):
        self.observers.append(observer)

    def Detach(self, observer):
        self.observers.remove(observer)

    def Notify(self):
        for observer in self.observers:
            observer.Update()

    def GetState(self):
        return self.subjectState

    def SetState(self):
        if self.subjectState:
            self.subjectState = False
        else:
            self.subjectState = True
        self.Notify()
