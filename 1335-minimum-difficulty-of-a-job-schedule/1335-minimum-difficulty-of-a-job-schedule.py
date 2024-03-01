class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @lru_cache(None)
        def helper(index: int, currentMax: int, d: int) -> Tuple[bool, int]:
            if d > index + 1:
                return math.inf
            
            if index < 0:
                return currentMax
            
            
            return min(
                helper(index - 1, max(currentMax, jobDifficulty[index]), d),
                max(currentMax, jobDifficulty[index]) + helper(index - 1, 0, d - 1)
            )
            
        
        ans = helper(len(jobDifficulty) - 1, 0, d)
        
        return ans if ans != math.inf else -1
            
            
            
        
        
        