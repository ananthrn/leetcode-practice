class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        @cache
        def helper(n: int, target: int) -> int:
            if n == 0:
                return 1 if target == 0 else 0
            
            if target <= 0:
                return 0
            
            ans = 0
            
            for roll in range(1, k + 1):
                ans = (ans + helper(n - 1, target - roll)) % MOD
            
            return ans
        
        return helper(n, target)
                