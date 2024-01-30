class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def helper(houseIndex: int, colorIndex: int) -> int:
            if houseIndex == 0:
                return costs[houseIndex][colorIndex]
            
            return costs[houseIndex][colorIndex] + min([helper(houseIndex - 1, diffColorIndex) for diffColorIndex in range(0, 3) if diffColorIndex != colorIndex])
        
        
        n = len(costs)
        
        print(len(costs))
        return min([helper(n - 1, colorIndex) for colorIndex in range(0, 3)])
        