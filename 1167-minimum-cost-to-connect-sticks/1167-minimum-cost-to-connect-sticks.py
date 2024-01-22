class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        
        ans = 0
        while len(sticks) > 1:
            smallest = heapq.heappop(sticks)
            secondSmallest = heapq.heappop(sticks)
            
            ans += smallest + secondSmallest
            
            heapq.heappush(sticks, smallest + secondSmallest)
            
        return ans