class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevSources = 0
        totalBeams = 0
        for row in bank:
            numOnes = len(list(filter(lambda val: val == '1', row)))
            
            if numOnes > 0:
                totalBeams += prevSources * numOnes
                prevSources = numOnes
        
        return totalBeams
        