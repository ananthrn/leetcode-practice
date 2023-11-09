class Solution:
    def countHomogenous(self, s: str) -> int:
        currentCount = 0
        prevChar = ""
        totalAnswer = 0
        MOD = 1_000_000_007
        
        for char in s:
            if char != prevChar:
                totalAnswer = int(totalAnswer + int((currentCount) * (currentCount + 1))/2)%MOD
                prevChar = char
                currentCount = 1
            else:
                currentCount += 1
            # print("char: ", char)
            # print("currentCount, totalAnswer, prevChar: ", currentCount, totalAnswer, prevChar)
            # print()
        
        totalAnswer = int(totalAnswer + int((currentCount) * (currentCount + 1))//2)%MOD
        
        return totalAnswer
        
        