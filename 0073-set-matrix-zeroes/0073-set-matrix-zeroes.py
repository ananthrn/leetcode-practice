class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        
        m, n = len(matrix), len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for r in zeroRows:
            for c in range(n):
                matrix[r][c] = 0
        
        for c in zeroCols:
            for r in range(m):
                matrix[r][c] = 0
        