class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def helper(startIndex, currentIndex, currentMax) -> int:
            if currentIndex >= len(arr):
                return 0
            
            if currentIndex - startIndex + 1 >= k:
                totalMax = max(arr[currentIndex], currentMax)
                
                return totalMax * (currentIndex - startIndex + 1) + helper(currentIndex + 1, currentIndex + 1, 0)
            
            totalMax = max(arr[currentIndex], currentMax)
            
            return max(
                helper(startIndex, currentIndex + 1, totalMax),
                totalMax * (currentIndex - startIndex + 1) + helper(currentIndex + 1, currentIndex + 1, 0)
            )
        
        ans = helper(0, 0, 0)
        
        return ans