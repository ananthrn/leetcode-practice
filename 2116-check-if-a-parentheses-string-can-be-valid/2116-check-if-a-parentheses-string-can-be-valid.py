class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s)%2 == 1:
            return False
        
        op = clos = var = 0
        for ind, char in enumerate(s):
            if locked[ind] == '1':
                if char == "(":
                    op += 1
                else:
                    clos += 1
            else:
                var += 1
            
            if op - clos + var < 0:
                return False
        
        op = clos = var = 0
        for ind in range(len(s) - 1, -1, -1):
            char = s[ind]
            
            if locked[ind] == '1':
                if char == ")":
                    op += 1
                else:
                    clos += 1
            else:
                var += 1
            
            if op - clos + var < 0:
                return False
            
            
        
        return True