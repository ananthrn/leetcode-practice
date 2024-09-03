class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        def dijkstra(src: int, dest: int) -> float:
            visited = set()
            PQ = [(-1.0, src)]
            
            while PQ:
                topProb, topNode = heapq.heappop(PQ)
                
                if topNode == dest:
                    return -topProb
                
                if topNode not in visited:
                    visited.add(topNode)
                    
                    for nextNode, nextWeight in adj[topNode]:
                        if nextNode not in visited:
                            heapq.heappush(PQ, (topProb * nextWeight, nextNode))
            
            return 0.0
                
        
        adj = collections.defaultdict(list)
        
        for (u, v), weight in zip(edges, succProb):
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        
        prob = dijkstra(start_node, end_node)
        
        return prob
        