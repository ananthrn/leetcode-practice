class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = n * [0]
        
        for u, v in edges:
            inDegree[v] += 1
        
        return list(filter(lambda ind: inDegree[ind] == 0, range(n)))
        