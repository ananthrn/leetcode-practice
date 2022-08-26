import itertools

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        val = 1
        twoPowers = set()
        
        while val <= int(1e9):
            twoPowers.add(tuple(sorted(str(val))))
            val *= 2
        
        stringRep = str(n)
        
        return tuple(sorted(stringRep)) in twoPowers
        # for val in itertools.permutations(stringRep):
        #     if val[0] != '0':
        #         perm = int(''.join(val))
        #         if perm in twoPowers:
        #             return True
        
        return False
        
            