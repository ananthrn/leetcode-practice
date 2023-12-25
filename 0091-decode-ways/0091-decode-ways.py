class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache
        def helper(s: str) -> int:
            if s == "":
                return 1
            
            if s[0] == '0':
                return 0
            
            if len(s) <= 1:
                return 1
            
            ans = 0
            
            if 1 <= int(s[:2]) <= 26:
                ans += helper(s[2:])
            ans += helper(s[1:])
            
            # print("s:", s)
            # print("ans:", ans)
            # print()
            return ans
        
        return helper(s)