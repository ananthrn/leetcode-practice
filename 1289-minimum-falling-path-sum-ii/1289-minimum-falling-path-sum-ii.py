class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @cache
        def helper(currentRow: int, prevColumn: int) -> int:
            if currentRow >= n:
                return 0
            
            mx = float("inf")
            for col in range(n):
                if col != prevColumn:
                    mx = min(mx, grid[currentRow][col] + helper(currentRow + 1, col))
            
            return mx
        
        return helper(0, -1)
            
            
        