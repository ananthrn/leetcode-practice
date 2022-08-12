from collections import defaultdict
from sortedcontainers import SortedDict

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = list(range(n))
        self.size = n * [1]
    
    def getParent(self, child: int) -> int:
        par = self.parent[child]
        
        if par != child:
            self.parent[child] = self.getParent(par)
        
        return self.parent[child]
    
    def check(self, x: int, y: int) -> bool:
        return self.getParent(x) == self.getParent(y)
    
    def union(self, x: int, y: int) -> None:
        par_x, par_y = self.getParent(x), self.getParent(y)
        
        if par_x == par_y:
            return
        
        if self.size[par_x] >= self.size[par_y]:
            self.parent[par_y] = par_x
            self.size[par_x] += self.size[par_y]
        else:
            self.parent[par_x] = par_y
            self.size[par_y] += self.size[par_x]
        
        
        
    
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        valToEdgeList = defaultdict(list)
        
        for edge in edgeList:
            valToEdgeList[edge[2]].append((edge[0], edge[1]))
        
        queriesIndex = [(i, query) for i, query in enumerate(queries)]
        queriesSorted = sorted(queriesIndex, key = lambda x: x[1][2])
        
        currentProcessed = -1
        
        ans = [None] * len(queries)
        
        UF = UnionFind(n)
        for (index, (a, b, edgeLength)) in queriesSorted:
            
            for lengthProcessed in range(currentProcessed + 1, edgeLength):
                for new_edge in valToEdgeList[lengthProcessed]:
                    UF.union(new_edge[0], new_edge[1])
            
            ans[index] = UF.check(a, b)
            currentProcessed = edgeLength - 1
        
        
        return ans
        