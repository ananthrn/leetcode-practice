class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        
        def euclideanDistance(bomb1,  bomb2):
            return (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2
        
        for ind1, bomb1 in enumerate(bombs):
            for ind2, bomb2 in enumerate(bombs):
                if euclideanDistance(bomb1, bomb2) <= (bomb1[2]) ** 2:
                    adj[ind1].append(ind2)
        
        
        
        def bfs(sourceIndex: int) -> int:
            seen = set()
            Q = collections.deque([sourceIndex])
            seen.add(sourceIndex)
            
            val = 0
            
            while Q:    
                tp = Q.pop()
                val += 1
                for nxt in adj[tp]:
                    if nxt not in seen:
                        seen.add(nxt)
                        Q.appendleft(nxt)
                        
            return val
        
        return max(bfs(sourceIndex) for sourceIndex in range(len(bombs)))
    