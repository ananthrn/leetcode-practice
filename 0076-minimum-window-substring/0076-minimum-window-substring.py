from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCtr = collections.Counter(t)
        sCtr = collections.Counter()
        
        bestString = None
        
        bestInterval = None
        left, right = 0, -1
        
        while right < len(s):
            if sCtr >= tCtr:
                if bestInterval is None or right -  left < bestInterval[1] - bestInterval[0]:
                    bestInterval = left, right
                sCtr[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    sCtr[s[right]] +=1
        
        
        return s[bestInterval[0]: bestInterval[1] + 1] if bestInterval is not None else ""
        
        
        