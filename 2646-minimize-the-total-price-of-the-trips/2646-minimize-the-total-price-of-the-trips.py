class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfsCounter(src: int, dest: int) -> collections.Counter:
            nonlocal adj
            Q = collections.deque([src])
            seen = set([src])
            prev = dict()
            prev[src] = src
            while Q:
                tp = Q.pop()
                if tp == dest:
                    break
                for nxt in adj[tp]:
                    if nxt not in seen:
                        seen.add(nxt)
                        prev[nxt] = tp
                        Q.appendleft(nxt)
            cnt = collections.Counter()
            cnt[dest] += 1
            cur = dest
            while cur != src:
                cur = prev[cur]
                cnt[cur] += 1
            
            return cnt 
        
        @cache
        def dp(src: int, par: int, canHalf: bool) -> int:
            nonlocal totalCount
            nonlocal adj
            if canHalf:
                sumHalved = totalCount[src] * price[src]//2
                
                for nxt in adj[src]:
                    if nxt!= par:
                        sumHalved += dp(nxt, src, False)
                
                sumNotHalved = totalCount[src] * price[src]
                
                for nxt in adj[src]:
                    if nxt != par:
                        sumNotHalved += dp(nxt, src, True)
                
                return min(sumHalved, sumNotHalved)
            
            else:
                sumNotHalved = totalCount[src] * price[src]
                
                for nxt in adj[src]:
                    if nxt != par:
                        sumNotHalved += dp(nxt, src, True)
                
                return sumNotHalved
                
                
        
        totalCount = collections.Counter()
        
        for src, dest in trips:
            bfsCount =  bfsCounter(src, dest)
            print("src, dest:" , src, dest)
            print("bfsCount: ", bfsCount)
            print()
            
            totalCount += bfsCount
            
        print("totalCount: ", totalCount)
        best = dp(0, -1, True)
        
        return best
            
        
        