from ASCIIConverter import ASCIIConverter
from RemoveTagUpper import RemoveTagUpper
from LeaveTagUpper import LeaveTagUpper

class Konfiguracja:
    def set_conterter(self, converter):
        if converter == "ASCII":
            return ASCIIConverter()
        elif converter == "RemoveTagUpper":
            return RemoveTagUpper()
        elif converter == "LeaveTagUpper":
            return LeaveTagUpper()
        #elif converter == "TagFormatConverter":
        #    return TagFormatConverter()
        else:
            raise NameError
