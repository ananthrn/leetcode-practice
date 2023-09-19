class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        seen = [0] * (n + 1)
        semester = [None] * (n + 1)
        
        adj = collections.defaultdict(list)
        
        for prereq, nextCourse in relations:
            adj[nextCourse].append(prereq)
            
        def dfs(src: int) -> bool:
            seen[src] = 1
            
            semester[src] = 1
            for nxt in adj[src]:
                if seen[nxt] == 1:
                    return False
                elif seen[nxt] == 2:
                    semester[src] = max(semester[src], semester[nxt] + 1)
                else:
                    check = dfs(nxt)
                    if not check:
                        return False
                    semester[src] = max(semester[src], semester[nxt] + 1)
            
            seen[src] = 2
            return True
        
        for i in range(1, n + 1):
            if seen[i] == 0:
                check = dfs(i)
            if not check:
                return -1
        
        return max(sem for sem in semester if sem is not None)
            
        