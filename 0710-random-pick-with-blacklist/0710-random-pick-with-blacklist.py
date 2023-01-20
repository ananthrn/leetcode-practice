class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.whiteListIndex = n - len(blacklist) - 1
        
        blackSet = set(blacklist)
        rightSideCandidates = [val for val in range(self.whiteListIndex + 1, n) if val not in blackSet]
        self.map = {}
        
        for blackVal in blacklist:
            if blackVal <= self.whiteListIndex:
                self.map[blackVal] = rightSideCandidates.pop()
        
    def pick(self) -> int:
        val = random.randint(0, self.whiteListIndex)
        
        return self.map.get(val, val)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()