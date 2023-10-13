class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [0 for _ in range(n+1)]
        
        for j in range(2, n + 1):
            dp[j] = min(dp[j-1] + cost[j-1], dp[j-2] + cost[j-2])
        
        print(dp)
        return dp[n]
        
            
        