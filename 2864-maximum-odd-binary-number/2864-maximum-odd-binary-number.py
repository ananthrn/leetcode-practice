class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        cnt = collections.Counter(s)
        
        bestBinaryString =  (cnt['1'] - 1) * "1" +  cnt['0'] * "0"  + "1"
        
        return bestBinaryString
        