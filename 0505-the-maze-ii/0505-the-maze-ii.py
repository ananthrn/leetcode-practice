from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        
        dirMap = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        
        def getNextPosition(r, c, direction) -> List[int]:
            dist = 0
            dir_r, dir_c = dirMap[direction]
            while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                r += dir_r
                c += dir_c
                dist +=1
            
            r -= dir_r
            c -= dir_c
            dist -= 1
            
            return r, c, dist
        
        Q = []
        seen = set()
        heapq.heappush(Q, (0, start[0], start[1]))
        
        while Q:
            steps, tp_r, tp_c = heapq.heappop(Q)
            
            if [tp_r, tp_c] == destination:
                return steps
            
            if (tp_r, tp_c) not in seen:
                seen.add((tp_r, tp_c))
                
                for direction in dirMap.keys():
                    nxt_r, nxt_c, dist = getNextPosition(tp_r, tp_c, direction)
                    
                    if (nxt_r, nxt_c) not in seen:
                        heapq.heappush(Q, (dist + steps, nxt_r, nxt_c))
        
        return -1