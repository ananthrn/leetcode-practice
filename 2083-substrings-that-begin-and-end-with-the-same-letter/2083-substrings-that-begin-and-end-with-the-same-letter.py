class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = collections.Counter(s)
        
        answer = 0
        
        for count in counter.values():
            answer += count
            
            if count >= 2:
                answer += (count * (count - 1))//2
        
        return answer
        