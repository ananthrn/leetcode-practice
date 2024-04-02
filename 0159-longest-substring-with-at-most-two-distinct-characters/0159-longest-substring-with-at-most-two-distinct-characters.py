class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        c = collections.Counter()
        ans = 0
        for right in range(len(s)):
            c[s[right]] += 1
            
            while len(c) > 2:
                c[s[left]] -= 1
                
                if c[s[left]] == 0:
                    del c[s[left]]
                
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans