class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        INF = 1_000_000_000
        
        adj = collections.defaultdict(dict)
        
        # edges without weights are considered to have a weight of INF
        for u, v, weight in edges:
            if weight != -1:
                adj[u][v] = weight
                adj[v][u] = weight

        
        def getModifiedEdges() -> List[List[int]]:
            newEdges = []
            
            for u, v, weight in edges:
                if weight != -1:
                    newEdges.append([u, v, weight])
                else:
                    if v in adj[u]:
                        newEdges.append([u, v, adj[u][v]])
                    else:
                        newEdges.append([u, v, INF])
                        
            return newEdges
        
        def runDijkstra(src: int, dest: int) -> int:
            visited = set()
            PQ = [(0, src)]
            
            while PQ:
                topDistance, topNode = heapq.heappop(PQ)
                if topNode == dest:
                    return topDistance
                if topNode not in visited:
                    visited.add(topNode)
                    
                    
                    for nextNode, nextWeight in adj[topNode].items():
                        if nextNode not in visited:
                            heapq.heappush(PQ, (topDistance + nextWeight, nextNode))
            return INF
        
        initialDistance = runDijkstra(source, destination)
        
        print("initialDistance: ", initialDistance)
        if initialDistance < target:
            return []
        
        if initialDistance == target:
            return getModifiedEdges()
        
        for u, v, weight in edges:
            if weight == -1:
                print(f"modifying {u} -> {v} to 1")
                adj[u][v] = adj[v][u] = 1
                
                newDistance = runDijkstra(source, destination)
                print(f"newDistance: {newDistance}")
                
                # you can reach the target
                if newDistance <= target:
                    # make up the difference with the edge you just modified
                    adj[u][v] += (target - newDistance)
                    adj[v][u] = adj[u][v]
                    return getModifiedEdges()
                # otherwise continue modifying other edges
                    
                
            
        return []
        