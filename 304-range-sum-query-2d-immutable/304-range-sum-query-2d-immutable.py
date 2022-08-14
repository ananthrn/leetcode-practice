class NumMatrix:
    
    def getValHelper(self, row, col, mat) -> int:
        m, n = len(mat), len(mat[0])
        
        if 0 <= row < m and 0 <= col < n:
            return mat[row][col]
        else:
            return 0
        
    def getPrefSums(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        print("m , n: ", m , n)
        prefSums = [n * [0] for i in range(m)]
        
        for row in range(m-1, -1, -1):
            for col in range(n - 1, -1, -1):
                prefSums[row][col] = (matrix[row][col] 
                + self.getValHelper(row + 1, col, prefSums)
                + self.getValHelper(row, col + 1, prefSums)
                - self.getValHelper(row + 1, col + 1, prefSums))
                val1 = matrix[row][col] 
                val2 = self.getValHelper(row + 1, col, prefSums)
                val3 = self.getValHelper(row, col + 1, prefSums)
                val4 = self.getValHelper(row + 1, col + 1, prefSums)
                # print("row, col: ", row, col)
                # print("mat, down, right, diag:", val1, val2, val3, val4)
                # print(" prefSums[row][col]", prefSums[row][col])
                # print()
        return prefSums
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefSums = self.getPrefSums(matrix)
        print(self.prefSums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        valTotal = self.getValHelper(row1, col1, self.prefSums) # row1, col1 to end
        valRight = self.getValHelper(row1, col2 + 1, self.prefSums) # row1, col2 + 1 to end
        valDown = self.getValHelper(row2 + 1, col1, self.prefSums) 
        valDiag = self.getValHelper(row2 + 1, col2 + 1, self.prefSums)
        
        
        return valTotal - valRight - valDown + valDiag # add back diagonal part since it is subtracted twice (once in valRight, once in valDiag)
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)