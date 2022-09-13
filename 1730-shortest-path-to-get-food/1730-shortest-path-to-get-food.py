from collections import deque
class Solution:
    
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def bfs(src) -> int:
            Q = deque([(0, src[0], src[1])])
            seen = set([tuple(src)])
            
            while len(Q) > 0:
                steps, r, c = Q.pop()
                
                for nxt_r, nxt_c in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if grid[nxt_r][nxt_c] == "#":
                            return steps + 1
                        if grid[nxt_r][nxt_c] == "O" and (nxt_r, nxt_c) not in seen:
                            seen.add((nxt_r, nxt_c))
                            Q.appendleft((steps + 1, nxt_r, nxt_c))
            
            return -1
        
        src = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == "*"][0]
        
        dist = bfs(src)
        
        return dist
        