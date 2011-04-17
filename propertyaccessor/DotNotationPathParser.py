import re

class DotNotationPathParser:
    def __init__(self):
        self.indexedRegex = re.compile("(.*)\[(\d+)\]")

    def parse(self, path):
        firstCut = path.split('.')
        keys = []
        for key in firstCut:
            regexResult = self.indexedRegex.search(key)
            if(regexResult != None):
                if(regexResult.group(1) != ''):
                    keys.append(regexResult.group(1))
                keys.append(int(regexResult.group(2)))
            else:
                keys.append(key)
        return keys

