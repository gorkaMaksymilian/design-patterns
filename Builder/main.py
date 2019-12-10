from HTMLReader import HTMLReader
from Konfiguracja import Konfiguracja

if __name__ == '__main__':
    tekst = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"

    reader = HTMLReader(tekst)
    acii = Konfiguracja().set_conterter("ASCII")
    leave = Konfiguracja().set_conterter("LeaveTagUpper")
    remove = Konfiguracja().set_conterter("RemoveTagUpper")

    reader.change_converter(acii)
    print(f"HTML bez tagow:\n{''.join(reader.ParseHTML())}\n")

    reader.change_converter(leave)
    print(f"HTML upper z tagami:\n{''.join(reader.ParseHTML())}\n")

    reader.change_converter(remove)
    print(f"HTML upper bez tagow:\n{''.join(reader.ParseHTML())}\n")
