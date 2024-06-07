class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        maxObstaclesPossible = m + n - 1
        
        Q = collections.deque([(0, 0, 0)])
        
        
        dist = [
            [
                inf
            ] * n for _ in range(m)
        ]
        
        # dist[0][0] = 0
        
        while Q:
            r, c, obstaclesSeen = Q.popleft()
            # print("r, c, obstaclesSeen: ", r, c, obstaclesSeen)
            if dist[r][c] == inf:
                dist[r][c] = min(obstaclesSeen, dist[r][c])
                for nxt_r, nxt_c in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),                
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n and dist[nxt_r][nxt_c] == inf:
                        newObstacles = grid[nxt_r][nxt_c] + obstaclesSeen
                        # dist[nxt_r][nxt_c] = newObstacles
                        if grid[nxt_r][nxt_c] == 0:

                            Q.appendleft((nxt_r, nxt_c, newObstacles))
                        else:
                            Q.append((nxt_r, nxt_c, newObstacles))

        return dist[-1][-1]