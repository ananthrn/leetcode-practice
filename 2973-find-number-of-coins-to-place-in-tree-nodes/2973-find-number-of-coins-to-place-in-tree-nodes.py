import sortedcontainers
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        coins = n * [0]
        
        adj = collections.defaultdict(list)
        
        costList = collections.defaultdict(sortedcontainers.SortedList)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        def dfs(src, par):
            
            costList[src].add(cost[src])
            
            for nxt in adj[src]:
                if nxt != par:
                    dfs(nxt, src)
                    costList[src].update(costList[nxt])
            
            del costList[src][3:-3]
            
            if len(costList[src]) < 3:
                coins[src] = 1
            else:
                mx = 0
                
                mx = max(
                    mx,
                    costList[src][-1] * costList[src][-2] * costList[src][-3],
                    costList[src][-1] * costList[src][-2] * costList[src][0],
                    costList[src][-1] * costList[src][1] * costList[src][0],
                    costList[src][2] * costList[src][1] * costList[src][0],
                )
                coins[src] = mx
            
            # print("src: ", src)
            # print("costList[src]: ", costList[src])
            # print("coins[src]: ", coins[src])
            # print()
        
        dfs(0, -1)
        
        return coins