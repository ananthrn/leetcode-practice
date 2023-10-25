class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        
        totalApples = 0
        
        n = len(apples)
        
        maxDay = max([ind + days[ind] for ind in range(n)])
        for ind in range(maxDay):
            
            if ind < n:
                numApples = apples[ind]
                numDays = days[ind]
                heapq.heappush(heap, (ind + numDays - 1, numApples))
            
            
            while heap and heap[0][0] < ind:
                heapq.heappop(heap)
                
            if len(heap) == 0 and ind >= n:
                return totalApples
            if len(heap) > 0:
                expiryDay, numApples = heapq.heappop(heap)
                # print("expiryDay, numApples: ", expiryDay, numApples)
                # if expiryDay > ind:
                totalApples += 1

                if numApples > 1:
                    heapq.heappush(heap, ( expiryDay, numApples - 1))
                    
                    
            # print("ind: ", ind)
            # print("totalApples: ", totalApples)
            # print("heap: ", heap)
            # print()
        
        return totalApples
        
        