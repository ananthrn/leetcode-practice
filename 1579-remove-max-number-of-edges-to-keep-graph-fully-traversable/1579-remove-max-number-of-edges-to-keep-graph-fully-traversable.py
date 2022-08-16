class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n+ 1))
        self.comps = n
        
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def check(self, x: int, y: int) -> int:
        return self.find(x) == self.find(y)
    
    def union(self, x: int, y: int) -> None:
        par_x, par_y = self.find(x), self.find(y)
        
        
        if par_x != par_y:
            self.par[par_x] = par_y
            self.comps -= 1
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)
        
        for typ, a, b in edges:
            edgeMap[typ].append((a, b))
        
        res = e1 = e2 = 0
        uf1, uf2 = UnionFind(n), UnionFind(n)
        
        for a, b in edgeMap[3]:
            print(f"3 edge: {a}, {b}")
            print("exists? ", uf1.check(a, b), uf2.check(a, b))
            print()
            if uf1.check(a, b) == False or uf2.check(a, b) == False:
                e1 += 1
                e2 += 1
                uf1.union(a, b)
                uf2.union(a, b)
            else:
                res += 1
        
        for a, b in edgeMap[2]:
            # print(f"2 edge: {a}, {b}")
            # print("exists? ", uf2.check(a, b))
            # print()
            if uf2.check(a, b) == False:
                # e1 += 1
                e2 += 1
                uf2.union(a, b)
            else:
                res += 1
        
        for a, b in edgeMap[1]:
            # print(f"1 edge: {a}, {b}")
            # print("exists? ", uf1.check(a, b))
            # print()
            if uf1.check(a, b) == False:
                e1 += 1
                # e2 += 1
                uf1.union(a, b)
            else:
                res += 1
        
        print(uf1.comps, uf2.comps)
        if uf1.comps == 1 and uf2.comps == 1:
            return res
        else:
            return -1 
        
        