class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = (numPeople + 1) * [None]
        MOD = 1_000_000_007
        dp[0] = 1
        
        for ind in range(1, numPeople + 1):
            if ind % 2== 1:
                dp[ind] = 0
            else:
                total = 0
                
                for nextInd in range(1, ind):
                    total = (total + (dp[nextInd - 1] * dp[ind - nextInd - 1]) %MOD)%MOD
                
                dp[ind] = total
        
        
        return dp[numPeople]
                                     
                                     
        