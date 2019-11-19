class Wektor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

