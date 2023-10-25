class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)
        
        maxNumRoads = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                decrement = 1 if j in adj[i] else 0
                maxNumRoads = max(maxNumRoads, len(adj[i]) + len(adj[j]) - decrement)
        
        return maxNumRoads
        