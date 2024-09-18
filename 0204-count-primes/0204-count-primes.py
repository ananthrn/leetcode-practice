class Solution:
    def countPrimes(self, n: int) -> int:
#         def isPrime(val: int) -> bool:
#             i = 2
            
#             while i * i <= val:
#                 if (val % i) == 0:
#                     return False
#                 i += 1
            
#             return True
        
#         primes = list(filter(isPrime, range(2, n)))
        
#         return len(primes)
        
        # MAX = n
        composites = set([1])
        
        numPrimes = 0
        for currentValue in range(2, int(sqrt(n)) + 1):
            if currentValue not in composites:
                numPrimes += 1
                multiple = currentValue
                
                while multiple * currentValue < n:
                    composites.add(multiple * currentValue)
                    multiple += 1
        
        # print("composites: ", composites)
        return (n - 1) -  len(composites) if n > 1 else 0
            