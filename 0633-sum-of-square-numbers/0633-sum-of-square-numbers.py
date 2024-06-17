class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareSet = set(
            [
                ind * ind for ind in range(0, int(ceil(sqrt(c)) + 1))
            ]
        )
        
        print(squareSet)
        
        for sq in squareSet:
            if c - sq in squareSet:
                return True
            
        return False
        