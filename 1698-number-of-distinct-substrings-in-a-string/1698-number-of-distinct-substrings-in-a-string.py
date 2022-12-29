class Solution:
    def countDistinct(self, s: str) -> int:
        cnt = collections.Counter()
        MOD = 1_000_000_007
        for ind in range(len(s)):
            NUM = 0
            for ind2 in range(ind, len(s)):
                NUM = NUM * 27 + (ord(s[ind2]) - ord('a')) + 1
                # print("s[ind:ind2+1]: ", s[ind:ind2+1])
                # print("NUM: ", NUM)
                cnt[NUM] += 1
        
        # print("cnt: ", cnt)
        return len(cnt.keys())
        