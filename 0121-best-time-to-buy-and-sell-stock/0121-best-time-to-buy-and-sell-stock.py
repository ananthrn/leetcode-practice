class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        ans = 0
        
        for ind in range(1, len(prices)):
            ans = max(ans, prices[ind] - mn)
            mn = min(prices[ind], mn)
        
        return ans
    
        