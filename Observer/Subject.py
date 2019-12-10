from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def Attach(self, observer):
        pass

    @abstractmethod
    def Detach(self, observer):
        pass

    @abstractmethod
    def Notify(self):
        pass
