import numpy as np
class RandomizedSet:

    def __init__(self):
        np.random.seed(42)
        self.l = []
        self.pos = {}
        
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.l.append(val)
        self.pos[val] = len(self.l) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        currentPos = self.pos[val]
        endPos = len(self.l) - 1
        endVal = self.l[-1]
        
        if endPos == currentPos:
            del self.pos[val]
            self.l.pop()
            return True
        self.l[currentPos], self.l[-1] = self.l[-1], self.l[currentPos]
        
        self.pos[val], self.pos[endVal] = endPos, currentPos
        
        self.l.pop()
        del self.pos[val]
        
        return True

    def getRandom(self) -> int:
        index = np.random.randint(0, len(self.l))
        return self.l[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()