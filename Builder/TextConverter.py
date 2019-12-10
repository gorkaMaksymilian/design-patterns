from abc import ABC, abstractmethod

class TextConverter(ABC):
    @abstractmethod
    def ConvertCharacter(self, char):
        pass

    @abstractmethod
    def ConvertHTMLTag(self, tag):
        pass
