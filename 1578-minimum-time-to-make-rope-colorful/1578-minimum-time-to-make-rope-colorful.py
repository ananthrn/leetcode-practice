class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        timeHeap = [-neededTime[0]]
        
        cost = 0
        for ind in range(1, len(colors)):
            if colors[ind] != colors[ind - 1]:
                if len(timeHeap) >= 2:
                    heapq.heappop(timeHeap)
                    cost += - sum(timeHeap)
                    
                timeHeap = [-neededTime[ind]]
            else:
                heapq.heappush(timeHeap, - neededTime[ind])
        
        if len(timeHeap) >= 2:
            heapq.heappop(timeHeap)
            cost += - sum(timeHeap)
        
        return cost
        