class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [n * [False] for _ in range(n)]
        
        for ind in range(n):
            dp[ind][ind] = 1
        
        mxVal = 1
        mxString = s[0]
        for dist in range(1, n):
            for r in range(0, n - 1 - dist + 1):
                dp[r][r + dist] = False
                
                if s[r] == s[r+dist]:
                    dp[r][r + dist] =  (dp[r + 1][r + dist - 1]) or (dist == 1)
                
                if dp[r][r + dist]:
                    mxString = s[r: r + dist + 1]
                # mxVal = max(mxVal, dp[r][r + dist])
        
        
        return mxString