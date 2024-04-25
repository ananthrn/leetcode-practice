class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = collections.defaultdict(int)
        
        for ind, char in enumerate(s):
            # dp[char] = max(dp[char], 1)
            best = 0
            for prev_ind in range(ord('a'), ord('z') + 1):
                if abs(ord(char) - prev_ind) <= k:
                    best = max(best, dp[chr(prev_ind)])
            
                    
            dp[char] = max(best + 1, dp[char])
            
        
        return max(dp.values(), default=0)
        