class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        MOD = 1_000_000_007
        adj = collections.defaultdict(list)
        
        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))
            
        def dijkstra(src: int):
            Q = []
            
            heapq.heappush(Q, (0, src))
            dist = collections.defaultdict(int)
            
            while Q:
                steps, tp = heapq.heappop(Q)
                
                if tp not in dist:
                    dist[tp] = steps
                    
                    for nxt, weight in adj[tp]:
                        if nxt not in dist:
                            heapq.heappush(Q, (steps + weight, nxt))
        
            return dist
    
        
        distanceToLastNode = dijkstra(n)
        
        @cache
        def helper(node: int) -> int:
            if node == n:
                return 1
            
            ans = 0
            for nxt, weight in adj[node]:
                if distanceToLastNode[nxt] < distanceToLastNode[node]:
                    ans = (ans + helper(nxt)) %MOD
            
            return ans
        
        ans = helper(1)
        
        return ans
        