# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def getRows(self,col, rowsToCheck, binaryMatrix ) -> bool:
        m, n = binaryMatrix.dimensions()
        return [row for row in rowsToCheck if binaryMatrix.get(row, col)]
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        
        start = 0 
        end = m -1
        best = m 
        
        rowsToCheck = list(range(m))
        calls = 0
        while start <= end:
            mid = (start + end)//2
            calls += len(rowsToCheck)
            newRowsToCheck = self.getRows(mid, rowsToCheck, binaryMatrix)
            
            if len(newRowsToCheck) > 0:
                best = min(best, mid)
                end = mid - 1
                rowsToCheck = newRowsToCheck
            else:
                start = mid + 1
        print("calls: ", calls)
        return best if best < m else -1
        