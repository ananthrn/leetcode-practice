from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        m ,n = len(grid), len(grid[0])
        
        def bfs(r, c):
            print("r, c: ", r, c)
            grid[r][c] = "#"
            Q = deque([(r, c)])
            
            while len(Q) > 0:
                tp_r, tp_c = Q.pop()
                
                for nxt_r, nxt_c in (
                    (tp_r, tp_c + 1),
                    (tp_r, tp_c - 1),
                    (tp_r + 1, tp_c),
                    (tp_r - 1, tp_c),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c <n:
                        if grid[nxt_r][nxt_c] == "1":
                            grid[nxt_r][nxt_c] = "#"
                            Q.appendleft((nxt_r, nxt_c))
            
                        
        
        numIslands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    numIslands += 1
                    bfs(r, c)
                    
        
        return numIslands 
        