class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.wells = n * [False]
    
    def checkSame(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def setWell(self, x: int):
        root_x = self.find(x)
        self.wells[root_x] = True
    
    def hasWell(self, x: int) -> bool:
        root_x = self.find(x)
        return self.wells[root_x]
    
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.wells[root_x] |= self.wells[root_y]
    
    
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        wellPipes = []
        
        for ind, wellCost in enumerate(wells):
            wellPipes.append((wellCost, ind, -1))
        
        for u, v, pipeCost in pipes:
            wellPipes.append((pipeCost, u - 1, v - 1))
        
        wellPipes = sorted(wellPipes)
        dsu = UnionFind(n)
        
        totalCost = 0
        for cost, u, v in wellPipes:
            if v == -1:
                # a well cost
                
                # if u is already supplied don't do anything.
                if dsu.hasWell(u):
                    continue
                #else add a well at u
                else:
                    print(f"setting well with cost: {cost} at node: {u}")
                    totalCost += cost
                    dsu.setWell(u)
                    
            else:
                # a pipe cost
                
                # if both u and v have wells or they are already connected don't do anything
                if (dsu.hasWell(u) and dsu.hasWell(v)) or dsu.checkSame(u, v):
                    continue
                else:
                    print(f"setting Pipe with cost: {cost} between nodes: {u} -- {v}")
                    totalCost += cost
                    dsu.union(u, v)
        
        
        return totalCost
                
            