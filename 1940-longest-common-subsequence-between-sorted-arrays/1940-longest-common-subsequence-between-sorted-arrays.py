class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        currentIndices = [0] * len(arrays)
        
        currentValue = 1
        currentStreak = []
        
        while currentValue <= 100:
            notFound = False
            for currentArrayIndex, currentIndex in enumerate(currentIndices):
                indexPointer = currentIndex
                
                while indexPointer < len(arrays[currentArrayIndex]) and arrays[currentArrayIndex][indexPointer] < currentValue:
                    indexPointer += 1
                
                if indexPointer >= len(arrays[currentArrayIndex]):
                    return currentStreak
                
                if arrays[currentArrayIndex][indexPointer] > currentValue:
                    notFound = True
            
            if notFound == False:
                currentStreak.append(currentValue)
            
            currentValue +=1
        
        return currentStreak
            