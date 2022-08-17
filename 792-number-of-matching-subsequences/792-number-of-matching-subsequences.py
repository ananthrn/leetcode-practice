from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        charToPosMap = defaultdict(list)
        
        # create map by finding next character
        for ind, char in enumerate(s):
            charToPosMap[char].append(ind)
        
        # for each word, finding each succesive character should happen in a new position
        def check(word) -> bool:
            currentPos = -1
            for char in word:
                ind = bisect_right(charToPosMap[char], currentPos)
                if ind < len(charToPosMap[char]):
                    currentPos = charToPosMap[char][ind]
                else:
                    return False
            
            return True
        
        nums = len([word for word in words if check(word)])
        
        return nums
                
        