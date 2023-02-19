class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int) -> int:
        
        
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return 0
        
        self.par[root_y] = root_x
        
        return 1
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        totalCells = m * n
        
        posToIndex = lambda r, c: r * n + c
        
        
        grid = set()
        
        islandChanges = []
        
        UF = UnionFind(totalCells)
        
        for r, c in positions:
            if (r, c) in grid:
                islandChanges.append(0)
            
            else:
                grid.add((r, c))
                islandDelta = 1
                
                for nxt_r, nxt_c in (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if (nxt_r, nxt_c) in grid:
                            delta = UF.union(posToIndex(r, c), posToIndex(nxt_r, nxt_c))
                            islandDelta -= delta
                            print("r, c: ", r, c)
                            print("nxt_r, nxt_c: ", nxt_r, nxt_c)
                            print("delta: ", delta)
                
                islandChanges.append(islandDelta)
        
        totalIslands = list(islandChanges)
        
        for ind in range(1, len(totalIslands)):
            totalIslands[ind] += totalIslands[ind - 1]
            
        return totalIslands
                
                
        