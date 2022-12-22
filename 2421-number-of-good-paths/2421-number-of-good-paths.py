class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = n * [1]
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            if self.size[root_x] < self.size[root_x]:
                root_x, root_y = root_y, root_x
            
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
    
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        valueToNodes = collections.defaultdict(list)
        
        for node, val in enumerate(vals):
            valueToNodes[val].append(node)
        
        dsu = UnionFind(len(vals))
        
        goodPaths = 0
        
        for val in sorted(valueToNodes.keys()):
            print("val: ", val)
            print("nodes: ", valueToNodes[val])
            
            for node in valueToNodes[val]:
                for neb in adj[node]:
                    if vals[neb] <= vals[node]:
                        dsu.union(node, neb)
            
            componentCounts = collections.Counter()
            
            for node in valueToNodes[val]:
                componentCounts[dsu.find(node)] +=1
            
            
            goodPaths += sum(
                [
                    (count * (count + 1))//2 for count in componentCounts.values()
                ]
            )
        
        return goodPaths
        
        
        