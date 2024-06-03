class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        currentIndex = 0
        
        for ind, c in enumerate(s):
            if t[currentIndex] == c:
                currentIndex += 1
            
            if currentIndex >= len(t):
                break
        
        return len(t) - currentIndex