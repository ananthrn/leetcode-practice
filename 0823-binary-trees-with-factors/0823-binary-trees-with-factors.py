class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        
        @cache
        def helper(rootVal: int) -> int:
            ans = 1
            
            for val in arr:
                if rootVal % val == 0 and (rootVal//val) in arr:
                    ans = (ans + helper(val) * helper(rootVal//val))%MOD
            
            return ans
        
        totalAns = 0
        
        for val in arr:
            totalAns  = (totalAns + helper(val))%MOD
        
        return totalAns
            