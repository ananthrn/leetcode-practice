class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        
        @cache
        def helper(rootVal: int):
            ans = 1
            for val in valSet:
                if val < rootVal and rootVal %val ==0 and (rootVal//val) in valSet:
                    ans = (ans +  (helper(val) * helper(rootVal//val))%MOD)%MOD
                    
            return ans
                
        valSet = set(arr)
        
        numTrees = 0
        
        for rootVal in valSet:
            numTrees = (numTrees + helper(rootVal))%MOD
        
        return numTrees