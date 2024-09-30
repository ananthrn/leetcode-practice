from sortedcontainers import SortedDict
class AllOne:

    def __init__(self):
        self.stringToValue = dict()
        self.valueToStrings = SortedDict()
    
    def _update(self, key: str, oldValue: int, newValue: int) -> None:
        if newValue > 0:
            self.stringToValue[key] = newValue
        else:
            del self.stringToValue[key]
            
        self.valueToStrings[oldValue].remove(key)
        if len(self.valueToStrings[oldValue]) == 0:
            del self.valueToStrings[oldValue]
        
        if newValue > 0:
            if newValue in self.valueToStrings:
                self.valueToStrings[newValue].add(key)
            else:
                self.valueToStrings[newValue] = set([key])

        
            
    def inc(self, key: str) -> None:
        if key not in self.stringToValue:
            self.stringToValue[key] = 1
            if 1 in self.valueToStrings:
                self.valueToStrings[1].add(key)
            else:
                self.valueToStrings[1] = set([key])
            
            return 
        
        oldValue = self.stringToValue[key]
        newValue = oldValue + 1
        
        
        self._update(key, oldValue, newValue)
        

    def dec(self, key: str) -> None:
        oldValue = self.stringToValue[key]
        newValue = oldValue - 1
        
        self._update(key, oldValue, newValue)
            
    def getMaxKey(self) -> str:
        if len(self.valueToStrings) == 0:
            return ""
        else:
            return next(iter(self.valueToStrings.values()[-1]))

    def getMinKey(self) -> str:
        if len(self.valueToStrings) == 0:
            return ""
        else:
            return next(iter(self.valueToStrings.values()[0]))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()