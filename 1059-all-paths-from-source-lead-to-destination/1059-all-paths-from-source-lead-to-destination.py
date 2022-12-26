class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        seen = collections.defaultdict(int)
        destinations = []
        
        adj  = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
         
        def getDestinations(src: int) -> bool:
            # also check for cycles:
            
            seen[src] = 1
            
            if len(adj[src]) == 0:
                destinations.append(src)
                seen[src] = 2
                return True
            
            for nxt in adj[src]:
                if nxt == src or seen[nxt] == 1:
                    # cycle
                    return False
                elif seen[nxt] == 0:
                    check = getDestinations(nxt)
                    # next node had a cycle
                    if not check:
                        return False
            
            seen[src] = 2
            
            return True
        
        check = getDestinations(source)
        
        print("check: ", check)
        print("destinations: ", destinations)
        #no cycles and only one destination
        return check and destinations == [destination]
        
                
        