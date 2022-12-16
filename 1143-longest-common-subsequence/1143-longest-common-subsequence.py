class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dp = [
            (n + 1) * [0] for _ in range(m + 1)
        ]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(
                        dp[r-1][c-1],
                        dp[r][c-1],
                        dp[r-1][c]
                    )
        
        return dp[m][n]
        