from collections import defaultdict, deque

class Solution:
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        
        seen = n * [False]
        
        def checkDetonate(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, r2 = bomb2
            
            return (x1 - x2)**2 + (y1 - y2)**2 <= r1**2
        
        adj = defaultdict(list)
        
        for ind1, bomb1 in enumerate(bombs):
            for ind2, bomb2 in enumerate(bombs):
                if checkDetonate(bomb1, bomb2):
                    adj[ind1].append(ind2)
        
        
        
        def bfs(src: int) -> int:
            seen = set([src])
            Q = deque([src])
            
            ans = 1 
            
            while len(Q) > 0:
                tp = Q.pop()
                
                for nxt in adj[tp]:
                    if nxt not in seen:
                        seen.add(nxt)
                        Q.appendleft(nxt)
                        ans += 1
            
            return ans
        
        
        
        return max([ bfs(src) for src in range(len(bombs))])
            
        
        
        