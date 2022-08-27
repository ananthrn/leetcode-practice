from collections import deque
from sortedcontainers import SortedList
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m, n = row, col
        
        grid = [n * [m * n] for _ in range(m)]
        
        
        for day, (cell_row, cell_col) in enumerate(cells):
            grid[cell_row - 1][cell_col - 1] = day + 1
            
        
        def bfs(currentDay) -> bool:
            # # print("currentDay: ", currentDay)
            initial = [(0, c) for c in range(n) if grid[0][c] > currentDay]
            # print("initial: ", initial)
            
            Q = deque(initial)
            seen = set(initial)
            
            while len(Q) > 0:
                
                tp_r, tp_c = Q.pop()
                # print("tp_r, tp_c: ", tp_r, tp_c)
                # print()
                for nxt_r, nxt_c in (
                    (tp_r, tp_c + 1),
                    (tp_r, tp_c - 1),
                    (tp_r + 1, tp_c),
                    (tp_r - 1, tp_c),
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if (nxt_r, nxt_c) not in seen and grid[nxt_r][nxt_c] > currentDay:
                            seen.add((nxt_r, nxt_c))
                            if nxt_r == m-1:
                                return True
                            Q.appendleft((nxt_r, nxt_c))
            
            return False
                            
            
            
        def dijkstra() -> int:
            pass
        
        
        bestDay, start, end = -1, 0, m*n
        
        while start <= end:
            mid = (start + end)//2
            
            check = bfs(mid)
            
            if check:
                bestDay = max(bestDay, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return bestDay
                
            
            
            
        