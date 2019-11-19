from Wektor3D import Wektor3D

class Wektor2D:
    def __init__(self, x, y):
        self._vector = Wektor3D(x, y, 0)

    def __add__(self, other):
        return Wektor2D(self._vector.x + other._vector.x, self._vector.y + other._vector.y)

    def __str__(self):
        return f"x = {self._vector.x}, y = {self._vector.y}"

    def __sub__(self, other):
        return Wektor2D(self._vector.x - other._vector.x, self._vector.y - other._vector.y)
