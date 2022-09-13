class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def check(word: str, pattern: str) -> bool:
            if len(word) != len(pattern):
                return False
            
            permPatternWord = {}
            permWordPattern = {}
            
            for char1, char2 in zip(pattern, word):
                if (char1 in permPatternWord and permPatternWord[char1] != char2) or (char2 in permWordPattern and permWordPattern[char2] != char1):
                    return False
                    
                permPatternWord[char1] = char2
                permWordPattern[char2] = char1
            return True
        
        return [word for word in words if check(word, pattern)]
            
                
        