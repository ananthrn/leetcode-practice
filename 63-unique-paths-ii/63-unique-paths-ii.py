class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [n * [0] for _ in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        for r in range(1, m):
            if obstacleGrid[r][0]:
                dp[r][0] = 0
            else:
                dp[r][0] = dp[r-1][0]
        
        for c in range(1, n):
            if obstacleGrid[0][c]:
                dp[0][c] = 0
            else:
                dp[0][c] = dp[0][c-1]
                
        
        for r in range(1, m):
            for c in range(1,  n):
                if obstacleGrid[r][c]:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] +dp[r][c-1]
        
        return dp[m-1][n-1]
            
            
        