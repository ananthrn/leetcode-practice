class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        prev = 0
        
        for ind in range(len(prices)):
            if ind == len(prices) - 1 or prices[ind] >= prices[ind+1]:
                profit += prices[ind] - prices[prev]
                prev = ind + 1
        
        return profit
        