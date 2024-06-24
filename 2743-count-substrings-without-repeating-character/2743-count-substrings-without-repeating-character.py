class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        left = 0
        cnt = collections.Counter()
        
        answer = 0
        
        for ind, val in enumerate(s):
            cnt[val] += 1
            
            while left < ind and cnt.most_common(1)[0][1] > 1:
                cnt[s[left]] -= 1
                left += 1
            
            answer += (ind - left + 1)
        
        return answer
                