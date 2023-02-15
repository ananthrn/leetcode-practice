class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
        
        charWord = dict()
        wordChar = dict()
        
        for char, word in zip(pattern, s.split(" ")):
            if char not in charWord and word not in wordChar:
                charWord[char] = word
                wordChar[word] = char
            
            if char in charWord:
                if charWord[char] != word:
                    return False
            
            if word in wordChar:
                if wordChar[word] != char:
                    return False
        
        return True
        