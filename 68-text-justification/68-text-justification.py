class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        startIndex = 0
        
        ans: List[str] = []
        while startIndex < len(words):
            nextIndex = startIndex + 1
            currentLength = len(words[startIndex])
            
            while nextIndex < len(words) and currentLength + 1 + len(words[nextIndex]) <= maxWidth:
                currentLength += 1 + len(words[nextIndex])
                nextIndex += 1
            
            totalWords = nextIndex - startIndex
            totalSpaces = maxWidth - currentLength + totalWords - 1
            totalExtraSpaces = maxWidth - currentLength
            
            
            currentSent = words[startIndex]
            
            
            
            if nextIndex == len(words) or totalWords == 1:
                for ind in range(startIndex + 1, nextIndex):
                    currentSent = currentSent + " " + words[ind]
                currentSent += totalExtraSpaces * " "
                ans.append(currentSent)
            else:
                spacesPerSlot = totalSpaces//(totalWords - 1)
                extraSpaceLength = totalSpaces % (totalWords - 1)
                for ind in range(startIndex + 1, nextIndex):
                    extraSpace = 1 if (ind - (startIndex + 1) < extraSpaceLength) else 0
                    
                    currentSent += (spacesPerSlot + extraSpace) * " "
                    currentSent += words[ind]
                ans.append(currentSent)
            startIndex = nextIndex
        
        return ans
            
                
        