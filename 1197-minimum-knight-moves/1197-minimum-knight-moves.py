from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        
        Q = deque([(0, 0, 0)])
        seen = set([(0, 0)])
        
        
        while len(Q) > 0:
            steps, tp_r, tp_c = Q.popleft()
            # print("steps, tp_r, tp_c: ",  steps, tp_r, tp_c)
            for nxt_r, nxt_c in (
                (tp_r + 2, tp_c + 1),
                (tp_r + 2, tp_c - 1),
                (tp_r - 2, tp_c + 1),
                (tp_r - 2, tp_c - 1),
                (tp_r + 1, tp_c + 2),
                (tp_r - 1, tp_c + 2),
                (tp_r + 1, tp_c - 2),
                (tp_r - 1, tp_c - 2),     
            ):
                if (nxt_r, nxt_c) not in seen:
                    seen.add((nxt_r, nxt_c))
                    if (nxt_r, nxt_c) == (x, y):
                        return steps + 1
                    Q.append((steps + 1, nxt_r, nxt_c))
            
        return -1
        