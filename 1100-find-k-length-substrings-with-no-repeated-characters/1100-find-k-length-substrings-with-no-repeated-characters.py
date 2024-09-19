class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        cnt = collections.Counter(s[:k])
        
        answer = 0
        
        if cnt.most_common(1)[0][1] == 1:
            answer += 1
            
        
        for index in range(k, len(s)):
            cnt[s[index]] += 1
            cnt[s[index - k]] -= 1
            
            if cnt.most_common(1)[0][1] == 1:
                answer += 1
        
        return answer
            