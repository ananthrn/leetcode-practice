class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        m, n = len(maze), len(maze[0])
        
        dirMap = {
            "u": (-1, 0),
            "d": (1, 0),
            "l": (0, -1),
            "r": (0, 1)
        }
        
        def getNextPosition(r, c, direction) -> List[int]:
            dist = 0
            dir_r, dir_c = dirMap[direction]
            while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                r += dir_r
                c += dir_c
                dist +=1
                if [r, c] == hole:
                    return r, c, dist
            
            r -= dir_r
            c -= dir_c
            dist -= 1
            
            return r, c, dist
        
        Q = []
        seen = set()
        heapq.heappush(Q, (0, "", ball[0], ball[1]))
        
        while Q:
            steps, path, tp_r, tp_c = heapq.heappop(Q)
            print("tp_r, tp_c: ", tp_r, tp_c)
            print("Steps: ", steps)
            print("path: ", path)
            print()
            if [tp_r, tp_c] == hole:
                return path
            
            if (tp_r, tp_c) not in seen:
                seen.add((tp_r, tp_c))
                
                for direction in dirMap.keys():
                    nxt_r, nxt_c, dist = getNextPosition(tp_r, tp_c, direction)
                    
                    if (nxt_r, nxt_c) not in seen:
                        heapq.heappush(Q, (dist + steps, path + direction, nxt_r, nxt_c))
        
        return "impossible"