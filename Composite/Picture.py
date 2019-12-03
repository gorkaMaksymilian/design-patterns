from Graphic import Graphic

class Picture(Graphic):
    def __init__(self):
        self.graphics = []

    def Draw(self):
        for g in self.graphics:
            g.Draw()

    def Add(self, graphic):
        self.graphics.append(graphic)

    def Remove(self, graphic):
        self.graphics.remove(graphic)

    def GetChild(self, intiger):
        return self.graphics[intiger]
