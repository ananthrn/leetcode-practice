class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        
        counter = collections.Counter()
        
        ans = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            print("right: ", right)
            while len(counter.keys()) > k:
                # print("left: ", left)
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
        