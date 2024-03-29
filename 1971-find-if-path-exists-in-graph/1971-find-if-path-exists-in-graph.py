class unionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.size = n * [1]
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
            
        if root_x != root_y:
            self.par[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = unionFind(n)
        
        for a, b in edges:
            uf.union(a, b)
        
        return uf.find(source) == uf.find(destination)
        