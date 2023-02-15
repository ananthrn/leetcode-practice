class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = list(map(lambda stone: - stone, stones))
        heapq.heapify(weights)
        
        while len(weights) >= 2:
            weight1 = -heapq.heappop(weights)
            weight2 = -heapq.heappop(weights)
            
            if weight1 > weight2:
                heapq.heappush(weights, - ( weight1 - weight2))
        
        return -weights[0] if len(weights) > 0 else 0
        