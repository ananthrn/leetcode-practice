class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        
        remainder = word1[minLen:] + word2[minLen:]
        
        return "".join(val1 + val2 for val1, val2 in zip(word1, word2)) + remainder