from Subject import Subject
from math import sqrt

class RealSubject(Subject):
    def licz(self, a, b, c):
        delta = (b*b) - (4 * a * c)
        if delta > 0:
            x1 = (-1) * b - sqrt(delta) / 2 * a
            x2 = (-1) * b + sqrt(delta) / 2 * a
            return x1, x2
        elif delta == 0:
            x0 = (-1) * b  / 2 * a
            return x0
        elif delta < 0:
            return None
