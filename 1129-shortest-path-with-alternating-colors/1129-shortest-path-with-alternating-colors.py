class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        RED = 0 
        BLUE = 1
        
        graph = [collections.defaultdict(list) for _ in range(2)]
        
        for u, v in redEdges:
            graph[RED][u].append(v)
            # graph[RED][v].append(v)
        
        for u, v in blueEdges:
            graph[BLUE][u].append(v)
        
        
        # distances = n * [math.inf]
        
        def BFS(startColor: int, src: int) -> List[int]:
            Q = collections.deque([(0, 0, startColor)])
            distances = dict()
            seen = set()
            while Q:
                tp, dist, color = Q.pop()
                
                if (tp, color) not in seen:
                    distances[tp] = min(dist, distances.get(tp, math.inf))
                    seen.add((tp, color))
                    
                    for nxt in graph[color][tp]:
                        if nxt not in seen:
                            Q.appendleft((nxt, dist + 1, 1 - color))
            
            return distances
            
            
        
        redDistances = BFS(RED, 0)
        blueDistances = BFS(BLUE, 0)
        
        print("redDistances: ", redDistances)
        print("blueDistances: ", blueDistances)
        
        distances = []
        
        for node in range(n):
            redDist = redDistances.get(node, -1)
            blueDist = blueDistances.get(node, - 1)
            
            if redDist == -1 and blueDist == -1:
                distances.append(-1)
            elif blueDist == -1:
                distances.append(redDist)
            elif redDist == -1:
                distances.append(blueDist)
            else:
                distances.append(min(redDist, blueDist))
                
        return list(map(lambda x: -1 if x == math.inf else x, distances))
                
            
        