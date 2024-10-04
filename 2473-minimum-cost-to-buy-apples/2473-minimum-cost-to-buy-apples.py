class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        def dijkstra(src: int):
            Q = [(0, src)]
            seen = set()
            
            while Q:
                dist, tp = heapq.heappop(Q)
                
                if tp not in seen:
                    seen.add(tp)
                    minPath[src][tp] = dist 
                    
                    for nxt, weight in adj[tp].items():
                        if nxt not in seen:
                            heapq.heappush(Q, (dist + weight, nxt))
        
        minPath = collections.defaultdict(lambda: collections.defaultdict(lambda: math.inf))
        adj = collections.defaultdict(dict)
        
        for index in range(1, n + 1):
            minPath[index][index] = 0
        
        
        for u, v, cost in roads:
            # minPath[u][v] = min(minPath[u][v], cost)
            # minPath[v][u] = min(minPath[v][u], cost)
            adj[u][v] = adj[v][u] = cost
        
        
        # for intermediate in range(1, n + 1):
        #     # newMinPath = copy.deepcopy(minPath)
        #     for startIndex in range(1, n + 1):
        #         for endIndex in range(1, n + 1):
        #             minPath[startIndex][endIndex] = min(
        #                 minPath[startIndex][endIndex],
        #                 minPath[startIndex][intermediate] + minPath[intermediate][endIndex]
        #             )
        
        # print(adj)
        
        for index in range(1, n + 1):
            dijkstra(index)
            
        answers = [0] * n
        
        
        for index in range(1, n + 1):
            answers[index - 1] = min(
                appleCost[nextIndex - 1] + minPath[index][nextIndex] + k * minPath[index][nextIndex] for nextIndex in range(1, n + 1)
            )
            # print(f"possible answers for {index}")
            # print(list((appleCost[nextIndex - 1], minPath[index][nextIndex], k * minPath[index][nextIndex]) for nextIndex in range(1, n + 1)))
        
        return answers
        