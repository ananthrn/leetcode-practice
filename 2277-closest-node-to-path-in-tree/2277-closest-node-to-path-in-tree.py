class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        dist = [n * [math.inf] for _ in range(n)]
        
        def bfs(src):
            Q = [src]
            dist[src][src] = 0
            while Q:
                tmp = []
                for tp in Q:
                    for nxt in graph[tp]:
                        if dist[src][nxt] == math.inf:
                            dist[src][nxt] = dist[src][tp] + 1
                            tmp.append(nxt)
                Q = tmp
        
        _ = [bfs(src) for src in range(n)]
        
        print("dist: ", dist)
        ans = []
        for start, end, node in query:
            shortestDistance = min(list(range(n)), key=lambda x: dist[start][x] + dist[x][end] + dist[x][node])
            ans.append(shortestDistance)
        
        return ans