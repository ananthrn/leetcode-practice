class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def convertToInteger(string: str) -> int:
            answer = 0
            
            for char in string:
                answer |= 1 << (ord(char) - ord('a'))
            
            return answer
        
        def check(allowed: int, word: int) -> bool:
            return allowed & word == word
        
        allowedInteger = convertToInteger(allowed)
        
        return len(list(filter(lambda word: check(allowedInteger, convertToInteger(word)), words)))
        