from abc import ABC, abstractmethod

class FileState(ABC):
    @abstractmethod
    def Open(self):
        pass

    @abstractmethod
    def Close(self):
        pass

    @abstractmethod
    def Read(self):
        pass

    @abstractmethod
    def Write(self):
        pass
