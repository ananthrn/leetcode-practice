from sortedcontainers import SortedList
import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c = collections.Counter()
        c[s[0]] += 1
        i, j = 0, 0
        
        n = len(s)
        
        ans = 1
        
        
        while i < n and j < n:
            # print("c: ", c)
            # print("len(c): ", len(c))
            # print("i, j: ", i, j)
            # print("s[i:j+1]: ", s[i: j + 1])
            # print()
            if len(c) <= 2:
                ans = max(ans, j - i +1)
                j += 1
                if j < n:
                    c[s[j]] += 1
            else:
                c[s[i]] -= 1
                if c[s[i]] == 0:
                    del c[s[i]]
                i +=1
            
        
        return ans
        
        