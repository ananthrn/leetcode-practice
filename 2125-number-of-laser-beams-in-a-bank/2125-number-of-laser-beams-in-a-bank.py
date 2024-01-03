class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevSources = 0
        totalBeams = 0
        for row in bank:
            numOnes = len([1 for val in row if val == '1'])
            
            if numOnes > 0:
                totalBeams += prevSources * numOnes
                prevSources = numOnes
        
        return totalBeams
        