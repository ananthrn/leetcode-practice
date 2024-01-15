class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        charToIndex = collections.defaultdict()

        for ind, char in enumerate(keyboard):
            charToIndex[char] = ind 
        
        currentIndex = 0

        ans = 0 

        for char in word:
            nextIndex = charToIndex[char]
            ans += abs(nextIndex - currentIndex)
            currentIndex = nextIndex

        return ans