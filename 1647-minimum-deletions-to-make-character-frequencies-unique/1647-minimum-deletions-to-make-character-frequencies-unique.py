from collections import Counter
from sortedcontainers import SortedList
class Solution:
    def minDeletions(self, s: str) -> int:
        currentEmpty = 0
        
        counter = Counter(s)
        
        cntList = [counter[c] for c in counter]
        
        cntMap = defaultdict(int)
        
        ans = 0
        
        unseenFrequencies = SortedList(list(range(0, max(cntList) + 1)))
        for cntVal in cntList:
            unseenFrequencies.discard(cntVal)
        
        # print("unseenFrequencies: ", unseenFrequencies)
        for cntVal in cntList:
            if cntMap[cntVal] > 0:
                currentGapIndex = unseenFrequencies.bisect_left(cntVal) - 1
                # print("cntVal: ", cntVal)
                # print("currentGapIndex: ", currentGapIndex)
                currentGap = unseenFrequencies[currentGapIndex]
                ans += (cntVal - currentGap)
                cntMap[currentGap] = 1
                if currentGap > 0:
                    unseenFrequencies.remove(currentGap)
            else:
                cntMap[cntVal] = 1
            
        
        return ans
                
                
        
        