class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        counterMaps = collections.defaultdict(collections.Counter)
        
        adj = collections.defaultdict(list)
        adjReversed = collections.defaultdict(list)
        inDegree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adjReversed[v].append(u)
            inDegree[v] += 1
        
        startingNodes = [node for node in range(n) if inDegree[node] == 0]
        # for node in startingNodes:
        #     counterMaps[node][colors[node]] += 1
            
        Q = collections.deque(startingNodes)
        visited = set()
        
        while Q:
            tp = Q.pop()
            
            currentCounter = collections.Counter()
            for prev in adjReversed[tp]:
                for key, val in counterMaps[prev].items():
                    if val > currentCounter[key]:
                        currentCounter[key] = val
                    
            counterMaps[tp] = currentCounter
            counterMaps[tp][colors[tp]] += 1
            
            if tp not in visited:
                visited.add(tp)
                
                for nxt in adj[tp]:
                    inDegree[nxt] -= 1
                    if nxt not in visited and inDegree[nxt] == 0:
                        Q.appendleft(nxt)
        
        if len(visited) < n:
            return -1
        
        return max(cnt.most_common()[0][1] for cnt in counterMaps.values())
        