class Solution:
    def checkWinningPosition(self, board: List[str]) -> bool:
        for row in board + list(zip(*board)):
            if ''.join(row) in ["XXX", "OOO"]:
                return True
        mainDiag = ''.join(f"{board[i][i]}" for i in range(3))
        secondDiag = ''.join(f"{board[i][2-i]}" for i in range(3))
        
        intersec = set([mainDiag, secondDiag]).intersection(set(["XXX", "OOO"]))
        if len(intersec) > 0:
            return True
        return False
    
    def boardToString(self, currentBoard: List[List[chr]]):
        str1 = ""
        
        for row in currentBoard:
            str1.join(row)
        
        return str1
    
    def validTicTacToe(self, board: List[str]) -> bool:
        currentBoard = [3 * [' '] for i in range(3)]
        
        boardList = [list(row) for row in board]
        boardSeen = set()
        
        def backtrack(r: int, c: int, val):
            print("currentBoard: ", currentBoard)
            print("val: ", val)
            # boardString = 
            if(str(currentBoard) in boardSeen):
                print("board seen: ")
                return False
            
            boardSeen.add(str(currentBoard))
            
            if(currentBoard == boardList):
                print("Dest reached")
                return True
            
            if(self.checkWinningPosition(currentBoard)):
                print("Winning position! ")
                return False
            
            for nxt_r in range(3):
                for nxt_c in range(3):
                    if board[nxt_r][nxt_c] == val and currentBoard[nxt_r][nxt_c] == ' ':
                        currentBoard[nxt_r][nxt_c] =  val
                        nxtVal = 'X' if val == 'O' else 'O'
                        # print("nxt_r, nxt_c, nxtVal: ", nxt_r, nxt_c, nxtVal)
                        nxtCheck = backtrack(nxt_r, nxt_c, nxtVal)
                        currentBoard[nxt_r][nxt_c] = ' '
                        if nxtCheck:
                            return True
            return False
        
        check = backtrack(0, 0, 'X')
        
        
        return check
        