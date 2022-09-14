class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        
        gates = [(r, c) for r in range(m) for c in range(n) if rooms[r][c] == 0]
        
        Q = deque([(0, gate[0], gate[1]) for gate in gates])
        seen = set(gates)
        
        while len(Q) > 0:
            steps, r, c = Q.pop()
            
            for nxt_r, nxt_c in (
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    if rooms[nxt_r][nxt_c] == INF:
                        rooms[nxt_r][nxt_c] = steps + 1
                        Q.appendleft((steps + 1, nxt_r, nxt_c))
        
        
        