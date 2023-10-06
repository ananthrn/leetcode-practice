class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def backtrack(k: int) -> int:
            mx = max([i * (k- i) for i in range(1, k - 1)], default=1)
            
            for i in range(1, k - 1):
                mx = max(mx, i * backtrack(k - i))
            
            return mx
        
        if n == 2:
            return 1
        return backtrack(n)