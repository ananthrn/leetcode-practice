from sortedcontainers import SortedList

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def dijkstra() -> int:
            Q = SortedList([(grid[0][0], 0, 0)])
            # Q = []
            # heapq.heappush(Q, (grid[0][0], 0, 0))
            seen = [n * [False] for _ in range(n)]
            
            while len(Q) > 0:
                maxTime, tp_r, tp_c = Q.pop(0)
                # maxTime, tp_r, tp_c = heapq.heappop(Q)
                if (tp_r, tp_c) == (n-1, n-1):
                    return maxTime
                # seen.add((tp_r, tp_c))
                
                
                if not seen[tp_r][tp_c]:
                    for nxt_r, nxt_c in (
                        (tp_r, tp_c + 1),
                        (tp_r, tp_c - 1),
                        (tp_r + 1, tp_c),
                        (tp_r - 1, tp_c),
                    ):
                        if 0 <= nxt_r < n and 0 <= nxt_c < n:
                            if not seen[nxt_r][nxt_c]:
                                nextTime = max(maxTime, grid[nxt_r][nxt_c])
                                Q.add((nextTime, nxt_r, nxt_c))
                                # heapq.heappush(Q, (nextTime, nxt_r, nxt_c))
                                
                seen[tp_r][tp_c] = True
            
            return -1
        
        ans = dijkstra()
        
        return ans