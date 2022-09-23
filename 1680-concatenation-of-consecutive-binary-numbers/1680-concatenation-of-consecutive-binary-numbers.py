class Solution:
    
    def concatenatedBinary(self, n: int) -> int:
        
        MOD = 10 **9 +7
        binPow = 18 * [1]
        
        for exp in range(1, 18):
            binPow[exp] = (binPow[exp- 1] * 2)%MOD
        
        
        total = 0
        
        for i in range(1, n+1):
            binRep = bin(i)
            length = len(binRep) - 2
            binPo = binPow[length]
            total = ((total * binPo)% MOD + i)%MOD
        
        return total
        