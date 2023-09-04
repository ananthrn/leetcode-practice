class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        startIndex = 0
        while startIndex < len(words):
            currentLength = len(words[startIndex])
            nextIndex = startIndex + 1
            while nextIndex < len(words) and currentLength + 1 + len(words[nextIndex]) <= maxWidth:
                currentLength += 1 + len(words[nextIndex])
                nextIndex += 1
                
            numWords = nextIndex - startIndex
            # numSpaces = maxWidth - currentLength
            # numSpacesPerSlot = numSpaces//(numWords - 1)
            # numExtraSpaces = numSpaces % (numWords - 1)
            
            print("numWords: ", numWords)
            print("words are: ", words[startIndex: nextIndex])
            
            # print("numSpaces: ", numSpaces)
            # print("numSpacesPerSlot: ", numSpacesPerSlot)
            # print("numExtraSpaces: ", numExtraSpaces)
            
            if nextIndex < len(words) and numWords > 1:
                numSpaces = maxWidth - currentLength
                numSpacesPerSlot = numSpaces//(numWords - 1)
                numExtraSpaces = numSpaces % (numWords - 1)
                currentAns = words[startIndex]
                # print("numSpaces: ", numSpaces)
                # print("numSpacesPerSlot: ", numSpacesPerSlot)
                # print("numExtraSpaces: ", numExtraSpaces)
                for index, word in enumerate(words[startIndex+1: nextIndex]):
                    extraSpace = 1 if index < numExtraSpaces else 0
                    # print("index: ", index)
                    # print("extraSpace: ", extraSpace)
                    currentAns +=  " " + " " * (extraSpace + numSpacesPerSlot) + word
                # print("currentAns: ", currentAns)
                # print("len(currentAns):" , len(currentAns))
                # print()
                ans.append(currentAns)
            else:
                currentAns = words[startIndex]
                for index, word in enumerate(words[startIndex +1: nextIndex]):
                    currentAns += " " + word
                
                currentAns += " " * (maxWidth - len(currentAns))
                # print("currentAns: ", currentAns)
                # print("len(currentAns):" , len(currentAns))
                # print()
                ans.append(currentAns)
                 # pass
            
            
            startIndex = nextIndex
        return ans