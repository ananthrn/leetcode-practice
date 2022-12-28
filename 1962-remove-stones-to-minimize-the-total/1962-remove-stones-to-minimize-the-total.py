class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for removal in range(k):
            val = -heapq.heappop(heap)
            val = val - (val//2)
            if val > 0:
                heapq.heappush(heap, -val)
            
            if len(heap) == 0:
                return 0
        
        return -sum(heap)