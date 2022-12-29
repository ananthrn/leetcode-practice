class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n: int) -> int:
            if  n == 1:
                return 0
            
            if n <= 3:
                return 2 if n == 3 else 1
            
            if n % 2 == 0:
                return 1 + helper(n // 2)
            else:
                if n%4 == 3:
                    return 1 + helper(n + 1)
                else:
                    return 1 + helper( n - 1)
            
        
        return helper(n)