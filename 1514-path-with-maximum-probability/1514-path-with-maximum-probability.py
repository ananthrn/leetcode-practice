from sortedcontainers import SortedList

class Solution:
    def dijkstra(self, n: int, start: int, end: int, adj: Dict[int, List[int]]) -> float:
        Q = SortedList([[1.0, start]])
        prob = dict()
        
        while(not len(Q) == 0):
            probNode, tpNode = Q.pop()
            
            prob[tpNode] = probNode
            
            if tpNode == end:
                return probNode
            
            for nxNode, succProb in adj.get(tpNode, []):
                if nxNode not in prob:
                    Q.add([succProb * probNode, nxNode])
        
        
        return prob.get(end, 0.0)
            
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            adj[edge[0]].append([edge[1], prob])
            adj[edge[1]].append([edge[0], prob])
                
        return self.dijkstra(n, start, end, adj)
        

        
        