from DotNotationPathParser import DotNotationPathParser

class PropertyAccessor:
    def __init__(self, data):
        self.data = data
        self.pathParser = DotNotationPathParser()
        self.keyTypes = [type(()), type([]), type({})]

    def getValue(self, path):
        return self._getValue(path)[0]

    def setValue(self, path, newValue):
        (currentItem,lastItem,lastKey) = self._getValue(path, True)
        if(type(lastItem) in self.keyTypes):
            lastItem[lastKey] = newValue
        elif(isinstance(currentItem, object)):
            setattr(lastItem, lastKey, newValue)

    def _getValue(self, path, fixKeyErrors=False):
        keySequence = self.pathParser.parse(path)
        currentItem = self.data
        lastItem = None
        lastKey = None
        for key in keySequence:
            lastItem = currentItem
            lastKey = key
            #array-ish
            if(isinstance(key, int)):
                currentItem = currentItem[key]
            #object-ish
            elif(hasattr(currentItem, key)):
                currentItem = getattr(currentItem, key)
            #dict-ish
            elif(hasattr(currentItem, '__getitem__')):
                try:
                    currentItem = currentItem[key]
                except KeyError as keyError:
                    if(fixKeyErrors):
                        if(key != keySequence[-1]):
                            currentItem[key] = {}
                            currentItem = currentItem[key]
                        else:
                            break
                    else:
                        raise keyError
            else:
                raise TypeError("Path not supported: " + path)
        return (currentItem, lastItem, lastKey)

