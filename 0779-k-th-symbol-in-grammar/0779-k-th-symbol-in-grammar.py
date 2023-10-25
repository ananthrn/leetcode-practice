class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        @cache
        def helper(n: int, k :int) -> int:
            # print("n, k: ", n, k)
            # assert 0 <= k < 2**n -1
            if n == 0:
                return 0
            
            checkPrev = helper(n - 1, k//2)
            
            dic = {
                0: [0, 1],
                1: [1, 0],
            }
            
            return dic[checkPrev][k%2]
        
        ans = helper(n - 1, k - 1)
        
        return ans
        