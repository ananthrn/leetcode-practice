from sortedcontainers import SortedList
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sl = SortedList(sticks)
        
        ans = 0
        while len(sl) > 1:
            val_0 = sl.pop(0)
            val_1 = sl.pop(0)
            
            ans += val_0 + val_1
            
            sl.add(val_0 + val_1)
        
        return ans
        