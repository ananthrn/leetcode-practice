class RandomizedSet:

    def __init__(self):
        self.valToPos = dict()
        self.lst = []
        
    def insert(self, val: int) -> bool:
        if val in self.valToPos:
            return False
        
        self.lst.append(val)
        self.valToPos[val] = len(self.lst) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToPos:
            return False
        
        pos = self.valToPos[val]
        newVal = self.lst[-1]
        
        self.lst[-1], self.lst[pos] = self.lst[pos], self.lst[-1]
        
        self.valToPos[newVal] = pos
        
        self.lst.pop()
        del self.valToPos[val]
        
        return True

    def getRandom(self) -> int:
        pos = random.randint(0, len(self.lst) - 1)
        
        return self.lst[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()