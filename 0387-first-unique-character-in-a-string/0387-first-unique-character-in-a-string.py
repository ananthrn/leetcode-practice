class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        
        for ind, char in enumerate(s):
            if cnt[char] == 1:
                return ind
        
        return -1