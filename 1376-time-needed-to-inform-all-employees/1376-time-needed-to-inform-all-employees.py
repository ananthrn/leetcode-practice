class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        timeInformed = n * [10000000]
        
        # REMINDER: DO NOT DO n * [[ ]] as it creates n references to the SAME list
        
        # adj = [ list() for i in range(n)]
        
        adj = defaultdict(list)
        
        for emp, man in enumerate(manager):
            if man != -1:
                adj[man].append(emp)
        
        def dfs(src, time) -> None:
            timeInformed[src] = time
            for emp in adj[src]:
                dfs(emp, time + informTime[src])
      
        dfs(headID, 0)
        
        return max(timeInformed)
        