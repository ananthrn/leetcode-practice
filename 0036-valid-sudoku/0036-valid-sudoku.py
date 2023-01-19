from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            c = Counter([int(val) for val in row if val != "."])
            if any(
                [cnt > 1 for cnt in c.values()]
            ):
                return False
        
        for i in range(9):
            col = [board[r][i] for r in range(9)]
            c = Counter([int(val) for val in col if val != "."])
            if any(
                [cnt > 1 for cnt in c.values()]
            ):
                return False
        
        for base_row in range(3):
            for base_col in range(3):
                c = Counter()
                for row in range(base_row*3, base_row*3 + 3):
                    for col in range(base_col*3, base_col*3 + 3):
                        if board[row][col]!= ".":
                            c[board[row][col]] += 1
                
                if any(
                    [cnt > 1 for cnt in c.values()]
                    ):
                    return False
        

        return True

