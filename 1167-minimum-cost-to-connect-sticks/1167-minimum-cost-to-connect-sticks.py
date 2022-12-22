from sortedcontainers import SortedList

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) >= 2:
            val_0 = heapq.heappop(sticks)
            val_1 = heapq.heappop(sticks)
            
            ans += val_0 + val_1
            
            heapq.heappush(sticks, val_0 + val_1)
        
        
        return ans
        