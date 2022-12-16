class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        
        rook_r, rook_c = None, None
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c
                    break
        
        pawns = 0
        
        for r in range(rook_r + 1, m):
            if board[r][rook_c] == 'p':
                pawns +=1
                break
            elif board[r][rook_c] == 'B':
                break
        
        for r in range(rook_r -1, -1, -1):
            if board[r][rook_c] == 'p':
                pawns +=1
                break
            elif board[r][rook_c] == 'B':
                break
        
        for c in range(rook_c + 1, n):
            if board[rook_r][c] == 'p':
                pawns +=1
                break
            elif board[rook_r][c] == 'B':
                break
        
        for c in range(rook_c - 1, -1, -1):
            if board[rook_r][c] == 'p':
                pawns +=1
                break
            elif board[rook_r][c] == 'B':
                break
        
        
        return pawns
        
        
        
        