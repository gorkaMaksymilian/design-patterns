from TextConverter import TextConverter

class ASCIIConverter(TextConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertHTMLTag(self, tag):
        return tag[3:-4]


