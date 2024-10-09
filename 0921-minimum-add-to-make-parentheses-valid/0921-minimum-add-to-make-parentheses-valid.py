class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        prefixSum = 0 
        answer = 0
        
        d = {
            "(": 1,
            ")": -1
        }
        
        for index, char in enumerate(s):
            prefixSum += d[char]
            
            if prefixSum < 0:
                answer += (-prefixSum)
                prefixSum = 0
                
        
        return answer + prefixSum