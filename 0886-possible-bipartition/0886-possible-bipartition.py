class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = collections.defaultdict(int)
        
        adj = collections.defaultdict(list)
        
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        def dfs(src, color):
            print("src, color: ", src, color)
            colors[src] = color
            
            for nxt in adj[src]:
                if colors[nxt] == 0:
                    check = dfs(nxt, -color)
                    if not check:
                        return False
                else:
                    if colors[nxt] == color:
                        return False
            
            return True
        
        
        for src in range(n):
            if colors[src] == 0:
                check = dfs(src, 1)
                if not check:
                    return False
        
        return True
            