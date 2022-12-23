class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def helper(index: int) -> int:
            if index >= n:
                return 0
            ans = helper(index + 1)
            for nxt in range(index + 1, n):
                ans = max(prices[nxt] - prices[index] + helper(nxt + 2), ans)
            
            return ans
        
        return helper(0)
        