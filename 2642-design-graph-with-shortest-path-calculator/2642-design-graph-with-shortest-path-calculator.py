class Graph:
    
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjacencyList = self.computeAdjacencyList(edges)
        self.shortestPaths = collections.defaultdict(dict)
        self.n = n
        self.updateAllPairsShortestPaths()
        
    def computeAdjacencyList(self, edges: List[List[int]]) -> collections.defaultdict:
        adjList = collections.defaultdict(list)
        
        for u, v, w in edges:
            adjList[u].append((v, w))
        
        return adjList
    
    def computeShortestPaths(self, src: int):
        # print("Src: ", src)
        Q = []
        heapq.heappush(Q, (0, src))
        seen = set()
        
        while Q:
            
            dist, tp = heapq.heappop(Q)
            # print("tp, dist: ", tp, dist)
            if tp not in seen:
                seen.add(tp)
                self.shortestPaths[src][tp] = dist
                
                for nxt, w in self.adjacencyList[tp]:
                    if nxt not in seen:
                        heapq.heappush(Q, (dist + w, nxt))
        
        # print("shortest Paths from src: ", dict(self.shortestPaths[src]))
        # print()
            
    def updateAllPairsShortestPaths(self) -> None:
        for src in range(self.n):
            self.computeShortestPaths(src)
           
    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adjacencyList[u].append((v, w))
        # self.computeShortestPaths(u)

    def shortestPath(self, node1: int, node2: int) -> int:
        self.computeShortestPaths(node1)
        return self.shortestPaths[node1].get(node2, -1)


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)