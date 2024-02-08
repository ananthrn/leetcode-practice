class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        dp = dict()
        
        dp[0] = 1
        dp[1] = k
        dp[2] = k * k 
        
        for j in range(3, n + 1):
            dp[j] = (k - 1) * dp[j - 2] + (k - 1) * dp[j - 1]
        
        print("dp: ", dp)
        return dp[n]
            
            
        