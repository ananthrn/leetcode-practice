class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        def getCount(src: int,) -> int:
            Q = collections.deque([src])
            cnt = 0
            
            while Q:
                tp = Q.popleft()
                
                if tp not in seen:
                    seen[tp] = True
                    cnt += 1
                    
                    for nxt in adj[tp]:
                        Q.append(nxt)
            
            return cnt
        
        
        seen = dict()
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        counts = []
        for src in range(n):
            if src not in seen:
                counts.append(getCount(src))
        
        
        overallSum = sum(counts)
        
        answer = sum([count * (overallSum - count) for count in counts])
        
        return answer//2