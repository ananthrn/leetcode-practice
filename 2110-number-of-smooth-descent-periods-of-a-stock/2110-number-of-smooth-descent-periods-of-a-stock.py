class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = n * [1]
        
        for i in range(1, len(prices)):
            if prices[i - 1] == prices[i] + 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        
        return sum(dp)
        