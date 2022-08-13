from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        currentEmpty = 0
        
        counter = Counter(s)
        
        cntList = [counter[c] for c in counter]
        
        cntMap = defaultdict(int)
        
        ans = 0
        
        for cntVal in cntList:
            if cntMap[cntVal] > 0:
                currentGap = cntVal - 1
                while currentGap > 0 and cntMap[currentGap] > 0:
                    currentGap -= 1
                
                ans += (cntVal - currentGap)
                cntMap[currentGap] = 1
            else:
                cntMap[cntVal] = 1
            
        
        return ans
                
                
        
        