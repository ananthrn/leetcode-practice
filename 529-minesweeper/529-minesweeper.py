from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        
        def countMines(r, c) -> int:
            count = 0
            for nxt_r in range(r-1, r + 2):
                for nxt_c in range(c - 1, c + 2):
                    if 0 <= nxt_r < m and 0 <= nxt_c < n:
                        if (nxt_r, nxt_c) != (r, c):
                            count += int(board[nxt_r][nxt_c] == "M")
            return count
                
        output = [n * ["#"] for _ in range(m)]
        
        Q = deque([tuple(click)])
        seen = set()
        
        while len(Q) > 0:
            r, c = Q.pop()
            
            if board[r][c] in ("M", "E"):
                if board[r][c] == "M":
                    board[r][c] = "X"
                    return board
                elif board[r][c] == "E":
                    countMine = countMines(r, c)
                    if countMine == 0:
                        board[r][c] = "B"
                        for nxt_r in range(r-1, r + 2):
                            for nxt_c in range(c - 1, c + 2):
                                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                                    if(nxt_r, nxt_c) != (r, c) and board[nxt_r][nxt_c] in ("M", "E"):
                                        Q.appendleft((nxt_r, nxt_c))
                    elif countMine > 0:
                        board[r][c] = str(countMine)
            
            
        
                        
        
        
        return board
            
        