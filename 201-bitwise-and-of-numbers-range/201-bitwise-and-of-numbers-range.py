class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        nums = right - left + 1
        
        def getVal(exp: int) -> int:
            val = 2**exp
            
            
            if nums > val:
            # a 0 has to appear, since it cycles through all numbers
            # and comes out the other side
                return 0
            else:
            # In this case it depends, [left...right] have the same value for this digit, if the digit = 1, return the whole val, else do not
                digitLeft = (left>>exp)%2
                digitRight = (right >> exp)%2
                
                return val if (digitLeft == 1 and digitRight ==1) else 0
        
        
        powers = {exp: getVal(exp) for exp in range(31)}
        print("powers: ", powers)
        return sum(powers.values())
            
            
                
        