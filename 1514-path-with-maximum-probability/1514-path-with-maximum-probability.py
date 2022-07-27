from sortedcontainers import SortedList

class Solution:
    def dijkstra(self, n: int, start: int, end: int, adj: Dict[int, List[int]]) -> float:
        Q = SortedList([[1.0, start]])
        prob = dict()
        
        while(not len(Q) == 0):
            probNode, tpNode = Q.pop()
            # del Q[0]
            
            prob[tpNode] = probNode
            
            if tpNode == end:
                return probNode
            
            for nxNode, succProb in adj.get(tpNode, []):
                if nxNode not in prob:
                    Q.add([succProb * probNode, nxNode])
        
        
        return prob.get(end, 0.0)
            
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = dict()
        for edge, prob in zip(edges, succProb):
            if(edge[0] in adj):
                adj[edge[0]].append([edge[1], prob])
            else:
                adj[edge[0]] = [[edge[1], prob]]
            
            if(edge[1] in adj):
                adj[edge[1]].append([edge[0], prob])
            else:
                adj[edge[1]] = [[edge[0], prob]]
                
        return self.dijkstra(n, start, end, adj)
        
        seen = n * [0]
        probMap = n * [0.0]
        

        
        