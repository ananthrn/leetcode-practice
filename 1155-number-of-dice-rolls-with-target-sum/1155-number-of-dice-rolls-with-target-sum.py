class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        cache = {}

        def helper(n, target) -> int:
            if n == 0:
                return 1 if target == 0 else 0
            
            if target <= 0:
                return 0
            
            if (n, target) in cache:
                return cache[(n, target)]

            ans = 0
            for diceRoll in range(1, k + 1):
                ans = (ans + helper(n-1, target -diceRoll))%MOD
            
            cache[(n, target)] = ans % MOD
            return ans % MOD
        
        return helper(n, target)
            

