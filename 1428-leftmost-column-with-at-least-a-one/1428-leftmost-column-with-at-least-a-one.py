# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def checkCol(self,col, binaryMatrix ) -> bool:
        m, n = binaryMatrix.dimensions()
        return any([binaryMatrix.get(r, col) for r in range(m)])
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        
        start = 0 
        end = m -1
        best = m 
        
        while start <= end:
            mid = (start + end)//2
            
            if self.checkCol(mid, binaryMatrix):
                best = min(best, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return best if best < m else -1
        