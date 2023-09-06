class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        
        heapq.heapify(blocks)
        
        while len(blocks) > 1:
            largest = heapq.heappop(blocks)
            second_largest = heapq.heappop(blocks)
            heapq.heappush(blocks, second_largest + split)
            
        return heapq.heappop(blocks)
        # return ans