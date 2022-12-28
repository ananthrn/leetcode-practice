class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = collections.defaultdict(int)
        cycles = collections.defaultdict(list)
        adj = collections.defaultdict(list)
        parent = dict()
        cycleNum = 0
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def getCyclesDfs(src, p):
            nonlocal adj, visited, parent, cycleNum
            if visited[src] == 2:
                return 
            
            if visited[src] == 1:
                # cycle detected
                cycleNum += 1
                cycle = []
                
                cur = p
                cycle.append(p)
                
                while cur != src:
                    cur = parent[cur]
                    cycle.append(cur)
                
                cycles[cycleNum] = cycle
                
                return
            
            parent[src] = p
            
            visited[src] = 1
            
            for nxt in adj[src]:
                if nxt != p:
                    getCyclesDfs(nxt, src)
            
            visited[src] = 2
        
        def getDistances(sources: List[int]):
            nonlocal adj
            Q = collections.deque([(0, src) for src in sources])
            dist = dict()
            
            while Q:
                steps, tp = Q.pop()
                
                if tp not in dist:
                    dist[tp] = steps
                    
                    for nxt in adj[tp]:
                        if nxt not in dist:
                            Q.appendleft((steps + 1, nxt))
            
            return [dist[i] for i in range(n)]
        
        getCyclesDfs(0, None)
        
        print("cycles: ", cycles)
        distances = getDistances(cycles[1])
        
        return distances