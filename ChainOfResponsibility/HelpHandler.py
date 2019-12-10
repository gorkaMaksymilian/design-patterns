from abc import ABC, abstractmethod

class HelpHandler(ABC):
    @abstractmethod
    def HandleHelp(self):
        pass

    @abstractmethod
    def ShowHelp(self):
        pass

