class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        
        def dfs(src):
            seen.add(src)
            
            r, c = src
            
            for nxt_r, nxt_c in (
                (r, c + 1),
                (r, c - 1),
                (r + 1, c),
                (r - 1, c),
            ):  
                if 0<= nxt_r < m and 0 <= nxt_c < n:
                    if grid[nxt_r][nxt_c] == 1 and (nxt_r, nxt_c) not in seen:
                        dfs((nxt_r, nxt_c))
        
        def bfs(src):
            Q = collections.deque([src])
            island = list()
            pathSignature = []
            while Q:
                tp_r, tp_c = Q.pop()
                
                island.append((tp_r - src[0], tp_c - src[1]))
                
                if (tp_r, tp_c) not in seen:
                    seen.add((tp_r, tp_c))
                    
                    for (nxt_r, nxt_c, direction) in (
                        (tp_r, tp_c + 1, "R"),
                        (tp_r, tp_c - 1, "L"),
                        (tp_r + 1, tp_c, "D"),
                        (tp_r - 1, tp_c, "U"),
                    ):
                        if 0<= nxt_r < m and 0 <= nxt_c < n:
                            if grid[nxt_r][nxt_c] == 1 and (nxt_r, nxt_c) not in seen:
                                Q.appendleft((nxt_r, nxt_c))
                                pathSignature.append(direction)
                
                pathSignature.append("0")
                    
            return "".join(pathSignature)
        
            
        m, n = len(grid), len(grid[0])
        
        islands = set()
        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in seen:
                    island = bfs((r, c))
                    islands.add(island)
        
        print("islands: ", islands)
        return len(islands)
        