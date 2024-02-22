class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def dfs(src: int, parent: int, dep: int):
            depth[src] = dep
            
            for nxt in adj[src]:
                if nxt != parent:
                    dfs(nxt, src, dep+1)
            
            # depth[src] += 1
        
        n = len(edges) + 1
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        depth = collections.defaultdict(int)
        
        dfs(0, -1, 0)
        
        print("depth from 0: ", depth)
        farthestNode = max(range(n), key = depth.get)
        
        depth = collections.defaultdict(int)
        
        dfs(farthestNode, -1, 0)
        
        print(f"depth from {farthestNode}: ", depth)
        return max(depth.values())
        
            