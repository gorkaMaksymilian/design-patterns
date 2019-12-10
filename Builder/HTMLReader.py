import re

class HTMLReader:
    def __init__(self, text):
        self.converter = None
        self.text = text

    def ParseHTML(self):
        index = 0
        output = []
        while index < len(self.text):
            if str(self.text[index]) != '<':
                output.append(self.converter.ConvertCharacter(str(self.text[index])))
                index += 1
            else:
                tag = re.search("<(\w)>(.+?)</(\w)>", self.text[index:])[0]
                output.append(self.converter.ConvertHTMLTag(tag))
                index += len(tag)

        return output


    def change_converter(self, converter):
        self.converter = converter
