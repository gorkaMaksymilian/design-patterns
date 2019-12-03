from abc import ABC, abstractmethod

class Graphic(ABC):
    @abstractmethod
    def Draw(self):
        pass

    def Add(self, graphic):
        pass

    def Remove(self, graphic):
        pass

    def GetChild(self, intiger):
        pass
