from collections import defaultdict, Counter

class Solution:
    def getDenseRepr(self, mat: List[List[int]]) -> defaultdict:
        rep = defaultdict(Counter)
        m, n = len(mat), len(mat[0])
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] != 0:
                    rep[col][row] = mat[row][col]
        
        return rep
                
    
    def getSparseRepr(self, mat: defaultdict, m: int, n: int) -> List[List[int]]:
        rep = [n * [0] for _ in range(m)]
        
        for col, dic in mat.items():
            for row, val in dic.items():
                rep[row][col] = val
        
        return rep
    
    def denseAddition(self, vec1: Counter, vec2: Counter) -> Counter:
        
        return vec1 + vec2
    
    def denseAdditionList(self, vecList: List[Counter]) -> Counter:
        ans = Counter()
        
        for vec in vecList:
            ans.update(vec)
            
        return ans
    
    
    def denseScalarMultiplication(self, vec: Counter, scalar: float) -> Counter:
        ans = Counter()

        for ind, val in vec.items():
            ans[ind] = scalar * val
        
        return ans
    
    def denseMatrixVectorMultiplication(self, mat: defaultdict, vec: Counter) -> Counter: 
        
        vecListToSum = []
        
        # print("mat: ", mat)
        # print("vec: ", vec)
        
        for ind, scalar in vec.items():
            if ind in mat:
                # print("ind, scalar: ", ind, scalar)
                
                result = self.denseScalarMultiplication(mat[ind], scalar)
                # print("result: ", result)
                vecListToSum.append(result)
        
        # print("vecListToSum: ", vecListToSum)
        ans = self.denseAdditionList(vecListToSum)
        # print("denseMatrixVectorMultiplication: ", ans)
        # print()
        return ans
        
    def denseMatrixMultiplication(self, mat1: defaultdict, mat2: defaultdict) -> defaultdict:
        ans = defaultdict(Counter)
        
        for col_ind, vec in mat2.items():
            resultantVec = self.denseMatrixVectorMultiplication(mat1, vec)
            ans[col_ind] = resultantVec
        
        return ans
            
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])
        
        denseMat1 = self.getDenseRepr(mat1)
        denseMat2 = self.getDenseRepr(mat2)
        
        print("denseMat1: ", denseMat1)
        print("denseMat2: ", denseMat2)
        
        denseAns = self.denseMatrixMultiplication(denseMat1, denseMat2)
        
        ans = self.getSparseRepr(denseAns, m, n)
        
        return ans
        