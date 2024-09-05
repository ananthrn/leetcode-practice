class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        def dijkstra(src: int, threshold: int) -> int:
            visited = set()
            PQ = [(0, src)]
            
            numNodes = 0
            while PQ:
                topDist, topNode = heapq.heappop(PQ)
                
                if topNode not in visited:
                    visited.add(topNode)
                    numNodes += 1
                    
                    for nextNode, weight in adj[topNode]:
                        if topDist + weight <= threshold:
                            heapq.heappush(PQ, (topDist + weight, nextNode))            
            return numNodes
        
        adj = collections.defaultdict(set)
        
        for u, v, weight in edges:
            adj[u].add((v, weight))
            adj[v].add((u, weight))
            
        nodeList = sorted([
            (dijkstra(node, distanceThreshold), -node) for node in range(n)
        ])
        
        return -nodeList[0][1]
        
        
        