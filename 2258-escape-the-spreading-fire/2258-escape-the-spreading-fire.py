from collections import deque
class Solution:
    def getFireTimes(self, grid: List[List[int]], fires: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MAX_TIME = int(2e9)
        
        fireTimes = [n * [MAX_TIME] for _ in range(m)]
        
        Q = deque([(0, r, c) for (r, c) in fires])
        
        while len(Q) > 0:
            steps, r, c = Q.pop()
            if fireTimes[r][c] == MAX_TIME:
                fireTimes[r][c] = steps
                for nxt_r, nxt_c in (
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c),
                    (r - 1, c)
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if fireTimes[nxt_r][nxt_c] == MAX_TIME and grid[nxt_r][nxt_c] == 0:
                            Q.appendleft((steps + 1, nxt_r, nxt_c))
                        
        return fireTimes
    
    def bfs(self, grid, fireTimes, currentTime) -> bool:
        m, n = len(grid), len(grid[0])
        
        seen = [n * [False] for _ in range(m)]
        Q = deque()
        
        if fireTimes[0][0] > currentTime:
            Q.appendleft((currentTime, 0, 0))
            seen[0][0] = True
        
        while len(Q) > 0:
            steps, r, c = Q.pop()
            
            for nxt_r, nxt_c in (
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c),
                    (r - 1, c)
            ):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    if steps + 1 == fireTimes[nxt_r][nxt_c] and (nxt_r, nxt_c) == (m - 1, n - 1):
                        return True
                    if not seen[nxt_r][nxt_c] and steps + 1 < fireTimes[nxt_r][nxt_c] and grid[nxt_r][nxt_c] == 0:
                        seen[nxt_r][nxt_c] = True
                        if (nxt_r, nxt_c) == (m - 1, n - 1):
                            return True
                        Q.appendleft((steps + 1, nxt_r, nxt_c))
        
        return False
        
        
        
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fires = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
        fireTimes = self.getFireTimes(grid, fires)
        
        print(fireTimes)
        
        bestTime = -1
        start = 0
        end = int(1e9)
        
        
        while start <= end:
            mid = (start + end)//2
            
            check = self.bfs(grid, fireTimes, mid)
            
            if check:
                bestTime = max(bestTime, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return bestTime
        