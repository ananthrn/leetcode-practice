class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [i for i in range(n)]
    
    def getRoot(self, src: int) -> int:
        if self.par[src] == src:
            return src
        
        self.par[src] = self.getRoot(self.par[src])
        
        return self.par[src]
    
    def checkSame(self, src1: int, src2: int) -> bool:
        return self.getRoot(src1) == self.getRoot(src2)
    
    def union(self, src1: int, src2: int) -> None:
        check = self.checkSame(src1, src2)
        
        if check:
            return
        
        root1, root2 =  self.getRoot(src1), self.getRoot(src2)
                
        self.par[root1] = root2
        
        

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        comps = n
        UF = UnionFind(n)
        
        
        for time, src1, src2 in sorted(logs):
            if not UF.checkSame(src1, src2):
                UF.union(src1, src2)
                comps -= 1
                if comps == 1:
                    return time
        
        return -1
            
        