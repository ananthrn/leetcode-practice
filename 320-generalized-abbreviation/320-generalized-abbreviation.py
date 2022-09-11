class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        @cache
        def helper(start:int, end:int) -> List[str]:
            if end < start:
                return set([""])
            
            thisAns = set([word[start: end + 1], str(end - start + 1)])
            
            if start == end:
                return thisAns
            
            for i in range(start, end + 1):
                leftAns = helper(start, i - 1)
                rightAns = helper(i+1, end)
                
                abb1 = set([left + word[i] + right for left in leftAns for right in rightAns])
                
                thisAns |= abb1
            
            return thisAns
                
        
        ans = list(set(helper(0, len(word) - 1)))
        
        return ans
                
        