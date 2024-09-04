class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        
        adj = collections.defaultdict(list)
        
        for u, v, toll in highways:
            adj[u].append((v, toll))
            adj[v].append((u, toll))
        
        
        pastDiscountsAtNode = dict()
        PQ = [(0, discounts, 0)]
        
        while PQ:
            topDistance, topDiscounts, topNode = heapq.heappop(PQ)
            
            if topNode == n-1:
                return topDistance
            
            if topNode not in pastDiscountsAtNode or topDiscounts > pastDiscountsAtNode[topNode]:
                pastDiscountsAtNode[topNode] = topDiscounts
                
                for nextNode, nextToll in adj[topNode]:
                    # don't take the discount
                    heapq.heappush(
                        PQ,
                        (topDistance + nextToll, topDiscounts, nextNode)
                    )
                    
                    # take the discount if you have it
                    if topDiscounts >= 1:
                        heapq.heappush(
                            PQ,
                            (topDistance + nextToll//2, topDiscounts - 1, nextNode)
                            )
        return -1
        