from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        def bfs(target: int) -> int:
            #moves, pos, vel
            Q = deque([(0, 0, 1)])
            seen = set([(0, 1)])
            
            while len(Q) > 0:
                moves, pos, vel = Q.pop()
                
                if pos == target:
                    return moves
                
                if (pos + vel, vel * 2) not in seen:
                    # seen.add((pos + vel, vel * 2))
                    Q.appendleft((moves + 1, pos + vel, vel * 2))
                    
                if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                    if (pos, -vel//abs(vel)) not in seen:
                        # seen.add((pos, -vel//abs(vel)))
                        Q.appendleft((moves + 1, pos, -vel//abs(vel)))
            return -1
        
        return bfs(target)
            
        