class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(pattern, string, forward={}, backward={}):
            if len(pattern) == len(string) == 0:
                return True
            
            if (len(pattern) == 0) != (len(string) == 0):
                return False
            
            
            for length in range(1, len(string) - len(pattern) + 1 + 1):
                p, s = pattern[0], string[:length]
                
                if p not in forward and s not in backward:
                    forward[p] = s
                    backward[s] = p
                    
                    if helper(pattern[1:], string[length:], forward, backward):
                        return True
                    
                    del forward[p]
                    del backward[s]
                    
                elif p in forward and forward[p] == s and backward[s] == p:
                    if helper(pattern[1:], string[length:], forward, backward):
                        return True
                
                else:
                    pass
                    
            
            return False
        
        return helper(pattern, s)
        