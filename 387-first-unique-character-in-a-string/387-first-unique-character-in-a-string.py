from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        
        uniqueVals = [i for i, char in enumerate(s) if c[char] == 1]
        
        return min(uniqueVals) if len(uniqueVals) > 0 else -1
        