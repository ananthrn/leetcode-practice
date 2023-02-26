class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [(n + 1) *[1] for _ in range(m + 1)]
        
        dp[0][0] = 0
        
        for row in range(1, m + 1):
            dp[row][0] = row
        
        for col in range(1, n + 1):
            dp[0][col] = col
        
        for row in range(1, m + 1):
            for col in range(1, n  + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = min(
                        1 + dp[row-1][col-1],
                        1 + dp[row-1][col],
                        1 + dp[row][col-1]
                    )
        
        # print("dp: ", dp)
        
        return dp[m][n]
        