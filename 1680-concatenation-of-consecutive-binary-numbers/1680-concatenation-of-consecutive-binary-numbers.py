class Solution:
    
    def concatenatedBinary(self, n: int) -> int:
        def powMod(base, exp, MOD) -> int:
            if exp == 0:
                return 1
            if exp == 1:
                return base % MOD
            
            ansHalf = powMod(base, exp//2, MOD)
            ans = (ansHalf * ansHalf) % MOD
            
            if exp % 2 == 1:
                return (ans * base)%MOD
            else:
                return ans 
        
        MOD = 10 **9 +7
        binPow = 18 * [1]
        # binPow[1] = ÷
        
        for exp in range(1, 18):
            binPow[exp] = (binPow[exp- 1] * 2)%MOD
        
        
        total = 0
        
        for i in range(1, n+1):
            binRep = bin(i)
            length = len(binRep) - 2
            binPo = binPow[length]
            total = ((total * binPo)% MOD + i)%MOD
        
        return total
        