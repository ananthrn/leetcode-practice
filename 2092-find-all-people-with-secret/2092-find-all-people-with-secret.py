from collections import defaultdict, deque
from sortedcontainers import SortedList
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        timeEdge =defaultdict(list)
        
        times = SortedList([0])
        timeEdge[0] = [(0, firstPerson)]
        
        for a, b, time in meetings:
            timeEdge[time].append((a, b))
            
            if time not in times:
                times.add(time)
        
        secretHolders = {0}
        def bfsUpdateSecretHolders(adj, currentSecrets):
            Q = deque(list(currentSecrets))
            seen = set(currentSecrets)
            
            while len(Q) > 0:
                tp = Q.pop()
                
                for nxt in adj.get(tp, []):
                    if nxt not in seen:
                        secretHolders.add(nxt)
                        seen.add(nxt)
                        Q.appendleft(nxt)
            
                        
            
        for nextTime in times:
            adj = defaultdict(list)
            currentSecrets = set()
            
            for a, b in timeEdge[nextTime]:
                adj[a].append(b)
                adj[b].append(a)
                if a in secretHolders:
                    currentSecrets.add(a)
                if b in secretHolders:
                    currentSecrets.add(b)
                    
            bfsUpdateSecretHolders(adj, currentSecrets)
        
        return secretHolders
        