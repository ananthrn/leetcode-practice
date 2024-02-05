from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCtr = collections.Counter(t)
        sCtr = collections.Counter()
        
        bestString = None
            
        left, right = 0, -1
        
        while right < len(s):
            if sCtr >= tCtr:
                if bestString is None or right -  left + 1 < len(bestString):
                    bestString = s[left: right + 1]
                sCtr[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    sCtr[s[right]] +=1
        
        
        return bestString or ""
        
        
        