class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i >= n:
                return math.inf
            
            answer = min(
                cost[i] + dp(i + 1, remain - time[i] - 1),
                dp(i + 1, remain)
            )
            return answer
        
        n = len(cost)
        return dp(0, n)
        