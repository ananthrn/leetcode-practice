class Solution:
    def numSquares(self, n: int) -> int:
        dp = (n + 1) * [None]
        
        val = 0
        
        while val * val <= n:
            dp[val * val] = 1
            val += 1
        
        
        for j in range(n + 1):
            if dp[j] is None:
                dp[j] = j
                val = 1
                while val * val < j:
                    dp[j] = min(dp[j], 1+ dp[j - val*val])
                    val += 1
            
        
        return dp[n]
        
        