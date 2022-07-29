import numpy as np
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        wordlen = len(word)
        for row in board + list(zip(*board)):
            q = ''.join(row).split('#')
            for w in word, word[::-1]:
                for s in q:
                    if len(s) == wordlen and all([(w[i] == s[i]) or s[i] == ' ' for i in range(wordlen)]):
                        return True
                
        
        return False
        