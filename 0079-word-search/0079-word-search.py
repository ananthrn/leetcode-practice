class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(r, c, ind) -> bool:
            
            if word[ind] != board[r][c]:
                return False
            
            if ind >= len(word) - 1:
                return True
            
            board[r][c] = "#"
            for nxt_r, nxt_c in (
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ):
                if 0 <= nxt_r <m and 0 <= nxt_c < n:
                    check = helper(nxt_r, nxt_c, ind + 1)
                    if check:
                        return True
            
            board[r][c] = word[ind]
            
            return False
        
        m, n = len(board), len(board[0])
        
        
        
        return any(
            helper(r, c, 0) for r in range(m) for c in range(n)
        )
        