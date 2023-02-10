class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        oneSet = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
        
        Q = collections.deque([(r, c, 0) for (r, c) in oneSet])
        
        seen = set()
        
        maxDist = -1
        
        distMap = dict()
        
        while len(Q) > 0:
            tp_r, tp_c, dist = Q.pop()
            
            
            
            if (tp_r, tp_c) not in seen:
                if grid[tp_r][tp_c] == 0:
                    distMap[(tp_r, tp_c)] = dist
                    maxDist = max(maxDist, dist)
                    
                seen.add((tp_r, tp_c))
                
                for nxt_r, nxt_c in (
                    (tp_r + 1, tp_c),
                    (tp_r - 1, tp_c),
                    (tp_r, tp_c + 1),
                    (tp_r, tp_c - 1),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if (nxt_r, nxt_c) not in seen and grid[nxt_r][nxt_c] == 0:
                            Q.appendleft((nxt_r, nxt_c, dist + 1))
        print("distMap:", distMap)
        return maxDist
        
        
        