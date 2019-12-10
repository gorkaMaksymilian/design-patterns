from Subject import Subject
from RealSubject import RealSubject

class Proxy(Subject):
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.wynik = None

    def licz(self, a, b, c):
        if self.a != a or self.b != b or self.c != c:
            self.wynik = RealSubject().licz(a, b, c)
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Rozwiazanie z proxy')
        return self.wynik



