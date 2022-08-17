class Solution:
    def stringBad(self, s) -> bool:
        val = int(s)
        
        return val == 0 and s.startswith("00") or val > 0 and s.startswith("0")
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, dots) -> List[str]:
            
            if dots == 0:
                if int(s) > 255 or self.stringBad(s):
                    return []
                else:
                    return [s]
            
            ans = []
            for i in range(1, len(s)):
                
                if int(s[:i]) <= 255 and not self.stringBad(s[0:i]):
                    val = backtrack(s[i:], dots - 1)
                    for possAns in val:
                        ans.append(f"{s[:i]}.{possAns}")
            print("s", s)
            print("ans: ",  ans)
            print()
            return ans
        
        ans = backtrack(s, 3)
        
        return ans
                