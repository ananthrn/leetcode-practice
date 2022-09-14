class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        def isClosedIsland(r, c) -> bool:
            nonlocal seen
            Q = deque([(r, c)])
            # seen.add((r, c))
            
            reachedSide = False
            while len(Q) > 0:
                tp_r, tp_c = Q.pop()
                if tp_r in [0, m - 1] or tp_c in [0, n - 1]:
                    reachedSide = True
                    
                for nxt_r, nxt_c in (
                    (tp_r + 1, tp_c),
                    (tp_r - 1, tp_c),
                    (tp_r, tp_c + 1),
                    (tp_r, tp_c - 1),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if grid[nxt_r][nxt_c] == 0:
                            grid[nxt_r][nxt_c] = 1
                            Q.appendleft((nxt_r, nxt_c))
            
            return reachedSide == False
        
        count = 0
        for r in range(1, m-1):
            for c in range(1, n-1):
                if grid[r][c] == 0 and isClosedIsland(r, c):
                    count += 1
        
        return count
                    
                            
        