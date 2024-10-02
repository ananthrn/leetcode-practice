class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for val in arr:
            heapq.heappush(heap, (-abs(val - x), -val))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        
        arr = sorted(-val for dist, val in heap)
        
        return arr