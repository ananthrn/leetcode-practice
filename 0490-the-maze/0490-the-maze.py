from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def getNextPos(r, c, direction):
            dir_r, dir_c = dirMap[direction]
            
            while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                r += dir_r
                c += dir_c
            r -= dir_r
            c -= dir_c
            
            return (r, c)
        
        m, n = len(maze), len(maze[0])
        start_r, start_c = start
        
        dirMap = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0),
        }
        
        Q = deque()
        seen = set()
        
        Q.append((0, start_r, start_c))
        
        while len(Q) > 0:
            steps, r, c = Q.pop()
            
            if (r, c) == tuple(destination):
                return True
            
            if (r, c) not in seen:
                seen.add((r, c))
                for direction in dirMap:
                    nxt_r, nxt_c = getNextPos(r, c, direction)
                    
                    if 0 <= nxt_r < m and 0 <= nxt_c < n and (nxt_r, nxt_c) not in seen:
                        Q.appendleft((steps + 1, nxt_r, nxt_c))
        
        return False
                
                
                
                            
                            