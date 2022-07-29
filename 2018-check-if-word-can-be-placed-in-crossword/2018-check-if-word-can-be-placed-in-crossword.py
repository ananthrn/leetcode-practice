class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        def checkVerticalDown(r: int, c: int) -> bool:
            if(r > 0 and board[r-1][c] != '#'):
                return False
            # check vertically
            for j in range(len(word)):
                if(j + r >= m or (board[r+j][c] != ' ' and word[j] != board[r + j][c])):
                    return False
            
            if (len(word) + r >= m) or board[r + len(word)][c]=='#':
                return True
            
            return False
        
        def checkVerticalUp(r: int, c: int) -> bool:
            if(r <= m - 2 and board[r+1][c] != '#'):
                return False
            
            # check vertically
            for j in range(len(word)):
                if(r - j < 0 or (board[r -j][c] != ' ' and word[j] != board[r - j][c])):
                    return False
            
            if ( r - len(word) < 0 ) or board[r - len(word)][c]=='#':
                return True
            
            return False
        
        def checkHorizontalRight(r: int, c: int) -> bool:
            if(c > 0 and board[r][c-1] != '#'):
                return False
            # check horizontally
            for j in range(len(word)):
                if(j + c >= n or (board[r][j + c] != ' ' and word[j] != board[r][j+c])):
                    return False
            
            # check no space or different letter after
            
            if (len(word) + c >= n) or board[r][len(word)+c]=='#':
                return True
            
            return False
        
        def checkHorizontalLeft(r: int, c: int) -> bool:
            if(c <= n-2 and board[r][c+1] != '#'):
                return False
            # check horizontally
            for j in range(len(word)):
                if(c - j < 0 or (board[r][ c - j] != ' ' and word[j] != board[r][c - j])):
                    return False
            
            # check no space or different letter after
            
            if (c - len(word) < 0 ) or board[r][c - len(word)]=='#':
                return True
            
            return False
        
        for r in range(m):
            for c in range(n):
                print("r, c: ", r, c)
                # print("checkVert: ", checkVertical(r, c))
                # print("checkHoriz: ", checkHorizontal(r, c))
                # print()
                
                checkBoth = checkVerticalUp(r, c) or checkVerticalDown(r, c) or checkHorizontalRight(r, c) or checkHorizontalLeft(r, c)
                
                if checkBoth:
                    return True
                
        
        return False
        