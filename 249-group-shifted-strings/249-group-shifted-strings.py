from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shiftUp(string, shiftNum)-> str:
            charList = list(string)
            
            for ind, char in enumerate(charList):
                currentPos = ord(char) - ord('a')
                newPos = (shiftNum + currentPos)%26
                charList[ind] = chr(ord('a') + newPos)
            
            ans = ''.join(charList)
            return ans
        
        group = defaultdict(list)
        for string in strings:
            shiftNum = (26 - (ord(string[0]) - ord('a')))
            shiftedString = shiftUp(string, shiftNum)
            
            group[shiftedString].append(string)
        
        return group.values()