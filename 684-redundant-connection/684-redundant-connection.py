class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def check(self, x: int, y: int) ->bool:
        return self.find(x) == self.find(y)
    
    def union(self, x: int, y: int):
        if self.check(x, y):
            return
        
        root_x, root_y = self.find(x), self.find(y)
        
        self.par[root_y] = root_x
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        
        for a, b in edges:
            n = max(n, a, b)
        
        uf = UnionFind(n + 1)
        
        for a, b in edges:
            if uf.check(a, b):
                return (a, b)
            uf.union(a, b)
        
        return (-1, -1)
        