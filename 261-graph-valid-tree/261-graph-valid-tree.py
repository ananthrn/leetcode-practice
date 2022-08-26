
class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.comps = n
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False
        
        self.comps -= 1
        self.par[root_y] = root_x
        
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        nodes = set()
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        
        print("uf.comps: ", uf.comps)
        return uf.comps == 1
        
        