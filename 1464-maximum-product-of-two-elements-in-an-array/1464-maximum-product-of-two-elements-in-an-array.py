class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > 2:
                heapq.heappop(heap)
        
        return (heap[0] - 1) * (heap[1] - 1)
        