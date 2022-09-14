from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def bfsChange(src, islandNum):
            Q = deque([src])
            
            while len(Q) >0:
                r, c = Q.pop()
                grid[r][c] = islandNum
                
                for nxt_r, nxt_c in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if grid[nxt_r][nxt_c] == 1:
                            Q.append((nxt_r, nxt_c))
        
        def bfsShortestDistance(islandStart, islandEnd) -> int:
            startPositions = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == islandStart]
            Q = deque([(0, r, c) for r, c in startPositions])
            seen = set(startPositions)
            
            while len(Q) > 0:
                steps, r, c = Q.pop()
                
                for nxt_r, nxt_c in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if grid[nxt_r][nxt_c] == islandEnd:
                            return steps + 1
                        
                        if grid[nxt_r][nxt_c] == 0 and (nxt_r, nxt_c) not in seen:
                            seen.add((nxt_r, nxt_c))
                            Q.appendleft((steps + 1, nxt_r, nxt_c))
        
            return -1
        
        islandNum = 100
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    bfsChange((r, c), islandNum)
                    islandNum += 100
        
        print("grid: ", grid)
        
        distance = bfsShortestDistance(100, 200)
        
        return distance - 1
        
            
        