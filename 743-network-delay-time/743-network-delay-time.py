from sortedcontainers import SortedList
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(src: int) -> int:
            nonlocal dist, adj
            Q = SortedList([(0, src)])
            
            while len(Q) > 0:
                # print("Q: ", Q)
                steps, tp = Q.pop(0)
                # print("steps, tp: ", steps, tp)
                # print()
                if tp not in dist:
                    dist[tp] = steps
                
                    for nxtVal, time in adj[tp]:
                        if nxtVal not in dist:                
                            Q.add((steps + time, nxtVal))
        
                        
            
        adj = defaultdict(list)
        
        for u, v, time in times:
            adj[u].append((v, time))
            
        dist = {}
        
        dijkstra(k)
        
        if any([val not in dist for val in range(1, n + 1)]):
            return -1
        
        # print("dist: ", dist)
        return max(dist.values())
        
        
        
        