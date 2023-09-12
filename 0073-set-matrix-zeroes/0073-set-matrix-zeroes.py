class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        
        m, n = len(matrix), len(matrix[0])
        
        zeroFirstCol = False
        zeroFirstRow = False
        for r in range(m):
            if matrix[r][0] == 0:
                zeroFirstCol = True
        
        for c in range(n):
            if matrix[0][c] == 0:
                zeroFirstRow = True
                
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if zeroFirstCol:
            for r in range(m):
                matrix[r][0] = 0
        
        if zeroFirstRow:
            for c in range(n):
                matrix[0][c] = 0