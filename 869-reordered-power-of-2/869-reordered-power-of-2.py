import itertools

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        val = 1
        twoPowers = set()
        
        while val <= int(1e9):
            twoPowers.add(val)
            val *= 2
        
        stringRep = str(n)
        
        for val in itertools.permutations(stringRep):
            if val[0] != '0':
                perm = int(''.join(val))
                if perm in twoPowers:
                    return True
        
        return False
        
            