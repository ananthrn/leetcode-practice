class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        maxObstaclesPossible = m + n - 1
        
        Q = collections.deque([(0, 0, 0)])
        
        seen = set([])
        
        answer = maxObstaclesPossible
        
        bestAnswerForCell = [
            [maxObstaclesPossible + 1] * n for _ in range(m)
        ]
        
        while Q:
            r, c, obstaclesSeen = Q.popleft()
            # print("r, c, obstaclesSeen: ", r, c, obstaclesSeen)
            if (r, c) == (m - 1, n - 1):
                answer = min(answer, obstaclesSeen)
            else:
                if (r, c, obstaclesSeen) not in seen:
                    seen.add((r, c, obstaclesSeen))
                    
                    
                    if obstaclesSeen < answer and obstaclesSeen < bestAnswerForCell[r][c]:
                        for nxt_r, nxt_c in (
                            (r + 1, c),
                            (r - 1, c),
                            (r, c + 1),
                            (r, c - 1),
                        ):
                            bestAnswerForCell[r][c] = min(bestAnswerForCell[r][c], obstaclesSeen)
                            if 0 <= nxt_r < m and 0 <= nxt_c < n:
                                newObstacles = grid[nxt_r][nxt_c] + obstaclesSeen
                                
                                if (nxt_r, nxt_c, newObstacles) not in seen:
                                    if grid[nxt_r][nxt_c] == 0:
                                        Q.appendleft((nxt_r, nxt_c, newObstacles))
                                    else:
                                        Q.append((nxt_r, nxt_c, newObstacles))
                    
        
        
        return answer