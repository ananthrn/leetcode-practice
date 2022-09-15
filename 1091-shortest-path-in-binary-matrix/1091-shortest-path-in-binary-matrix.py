import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
       
        n = len(grid)
        Q = collections.deque()
        
        if grid[0][0] == 0:
            Q.appendleft((1, 0, 0))
            
        while len(Q) > 0:
            steps, r, c = Q.pop()
            
            if grid[r][c] == 0:
                if (r, c) == (n-1, n-1):
                    return steps
                
                grid[r][c] = 1
                
                for nxt_r in range(r-1, r+2):
                    for nxt_c in range(c-1, c+2):
                        if 0 <= nxt_r < n and 0 <= nxt_c < n:
                            if grid[nxt_r][nxt_c] == 0:
                                Q.appendleft((steps + 1, nxt_r, nxt_c))
        
        return -1