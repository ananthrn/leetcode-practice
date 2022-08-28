class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        diags = m + n - 1
        
        for rowDiag in range(m):
            
            diagElems = []
            
            ind = 0
            while (rowDiag + ind) < m and ind < n:
                diagElems.append(mat[rowDiag + ind][ind])
                ind += 1
            
            diagElems = sorted(diagElems)
            
            for diagInd, diagElem in enumerate(diagElems):
                mat[rowDiag + diagInd][diagInd] = diagElem
            
            
        for colDiag in range(1, n):
            diagElems = []
            
            ind = 0
            
            while ind < m and colDiag + ind < n:
                diagElems.append(mat[ind][colDiag + ind])
                ind += 1
            
            diagElems = sorted(diagElems)
            for diagInd, diagElem in enumerate(diagElems):
                mat[diagInd][colDiag + diagInd] = diagElem
        
        return mat
                
        