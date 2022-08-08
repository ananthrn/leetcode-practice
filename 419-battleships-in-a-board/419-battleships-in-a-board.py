class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        def dfs(r, c):
            board[r][c] = '#'
            
            for new_r, new_c in (
                (r, c + 1),
                (r, c - 1),
                (r + 1, c),
                (r - 1, c)
            ):
                if 0 <= new_r < m and 0 <= new_c < n:
                    if board[new_r][new_c] == 'X':
                        dfs(new_r, new_c)
        ships = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    dfs(r, c)
                    ships += 1
        
        return ships
        