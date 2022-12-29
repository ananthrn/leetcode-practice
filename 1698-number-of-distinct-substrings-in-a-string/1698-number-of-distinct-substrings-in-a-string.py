class Solution:
    def countDistinct(self, s: str) -> int:
        cnt = collections.Counter()
        
        for ind in range(len(s)):
            for ind2 in range(ind + 1, len(s)+1):
                cnt[s[ind:ind2]] +=1
        
        # print("cnt: ", cnt)
        return len(cnt.keys())
        