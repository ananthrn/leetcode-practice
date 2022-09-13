from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        Q = deque()
        seen = set()
        
        if grid[0][0] <= k:
            Q.appendleft((0, grid[0][0], 0, 0))
        
        ans = int(10**9)
        
        while len(Q) > 0:
            steps, obstacles, r, c = Q.pop()
            
            if (r, c) == (m-1, n -1):
                return steps
            
            if not (obstacles, r, c) in seen:
                seen.add((obstacles, r, c))
                
                for nxt_r, nxt_c in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        new_obst = obstacles + grid[nxt_r][nxt_c]
                        if new_obst <= k and (new_obst, nxt_r, nxt_c) not in seen:
                            Q.appendleft((steps + 1, new_obst, nxt_r, nxt_c))
        
        return -1 
        
        
        