import numpy as np

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = 12 * [0]
        cache = dict()
        
        def backtrack(index) -> int:
            
            while index < len(debt) and debt[index] == 0:
                index += 1
                
            if index == len(debt):
                return 0
            
            minTransactions = np.inf
            
            for next_index in range(index + 1, len(debt)):
                if debt[index] * debt[next_index] < 0:
                    debt[next_index] += debt[index]
                    
                    nextTransactions = backtrack(index + 1)
                    minTransactions = min(minTransactions, nextTransactions + 1)
                    debt[next_index] -= debt[index]
                
            return minTransactions
            
        
        for a, b, mon in transactions:
            debt[b] -= mon
            debt[a] += mon
        
        val = backtrack(0)
        
        return val
                    
            
                
        