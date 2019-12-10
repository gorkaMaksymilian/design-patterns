from TextConverter import TextConverter

class RemoveTagUpper(TextConverter):
    def ConvertCharacter(self, character):
        return character.lower()

    def ConvertHTMLTag(self, tag):
        tag_list = list(tag)
        for index in range(3, len(tag_list) - 4):
            tag_list[index] = str(tag_list[index]).upper()
        tag = ''.join(tag_list)
        return tag[3:-4]



