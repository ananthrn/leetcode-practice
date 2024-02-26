class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        def getAdjacencyListFromEdgeList(edgeList):
            adj = collections.defaultdict(list)
            relevantPeopleWithSecret = set()
            
            for u, v in edgeList:
                adj[u].append(v)
                adj[v].append(u)
                
                if u in peopleWithSecret:
                    relevantPeopleWithSecret.add(u)
                if v in peopleWithSecret:
                    relevantPeopleWithSecret.add(v)
                    
            
            return adj, relevantPeopleWithSecret
        
        def bfs(relevantPeopleWithSecret, adj: collections.defaultdict) -> Set[int]:
            nonlocal peopleWithSecret
            
            Q = collections.deque(relevantPeopleWithSecret)
            
            while Q:
                tp = Q.pop()
                
                for nxt in adj[tp]:
                    if nxt not in peopleWithSecret:
                        Q.appendleft(nxt)
                        peopleWithSecret.add(nxt)
                        
            # return srcNodes
                
        
        peopleWithSecret = set([0, firstPerson])
        
        timeToEdges = collections.defaultdict(list)
        
        for x, y, time in meetings:
            timeToEdges[time].append((x, y))
        
        
        for time in sorted(timeToEdges.keys()):
            adj, relevantPeopleWithSecret = getAdjacencyListFromEdgeList(timeToEdges[time])
            bfs(relevantPeopleWithSecret, adj)
        
        return list(peopleWithSecret)
            