from Picture import Picture
from Line import Line
from Rectangle import Rectangle
from Text import Text


aPicture = Picture()
aPicture.Add(Text())
aPicture.Add(Line())
aPicture.Add(Rectangle())


picture = Picture()
picture.Add(Line())
picture.Add(Rectangle())
picture.Add(aPicture)
picture.Add(Line())


picture.Draw()
