class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.mapDict = {}
        self.blacklist = set(blacklist)
        self.n = n
        
        currentIndex = n - len(blacklist)
        
        for val in blacklist:
            if val < n - len(blacklist):
                while currentIndex < n and currentIndex in self.blacklist:
                    currentIndex += 1
                if currentIndex < n:
                    self.mapDict[val] = currentIndex
                    currentIndex += 1
        
        print("self.mapDict: ", self.mapDict)
        
        

    def pick(self) -> int:
        val = random.randint(0, self.n - len(self.blacklist) - 1)
        
        return self.mapDict.get(val, val)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()