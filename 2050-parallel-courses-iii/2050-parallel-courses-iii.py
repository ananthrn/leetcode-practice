class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inDegree = n * [0]
        adj = collections.defaultdict(list)
        
        for u, v in relations:
            adj[u - 1].append(v - 1)
            inDegree[v-1] +=1
        
        totalTime = n * [0]
        
        Q = collections.deque()
        for node in range(n):
            if inDegree[node] == 0:
                totalTime[node] = time[node]
                Q.appendleft(node)
        
        while Q:
            tp = Q.pop()
            
            for nxt in adj[tp]:
                totalTime[nxt] = max(totalTime[nxt], time[nxt] + totalTime[tp])
                inDegree[nxt] -=1
                
                if inDegree[nxt] == 0:
                    Q.appendleft(nxt)
        
        return max(totalTime)
        
        