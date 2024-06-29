class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        @cache
        def dfs(src: int) -> Set[int]:
            
            answer = set()
            
            for nxt in adj[src]:
                answer.add(nxt)
                answer |= dfs(nxt)
            
            return answer
        
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[v].append(u)
        
        return [
            sorted(list(dfs(src))) for src in range(n)
        ]
        
        