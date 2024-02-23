class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        def dijkstra(src: int, maxEdges: int, dst: int) -> int:
            nonlocal adj
            
            queue = []
            seen = dict()
            
            heapq.heappush(queue, (0, 0, src))
            
            found = False
            bestDist = math.inf
            
            while queue:
                dist, jumps, tp = heapq.heappop(queue)
                
                # print(f"tp: {tp}, jumps: {jumps}, dist: {dist}")
                
                if tp == dst:
                    
                    found = True
                    bestDist = min(bestDist, dist)
                    # print(f"Found {tp} at dst: {dist}. Bestdst: {bestDist}")
                
                if (tp, jumps) not in seen:
                    seen[(tp, jumps)] = True
                    
                    for nxt, edgeLength in adj[tp]:
                        if (nxt, jumps + 1) not in seen and jumps + 1 <= maxEdges:
                            heapq.heappush(queue, (dist + edgeLength, jumps + 1, nxt))
            
            return -1 if not found else bestDist
        
        adj = collections.defaultdict(list)
        
        for u, v, price in flights:
            adj[u].append((v, price))
            # adj[v].append(u)
        
        dist = dijkstra(src, k + 1, dst)
        
        return dist
        
            