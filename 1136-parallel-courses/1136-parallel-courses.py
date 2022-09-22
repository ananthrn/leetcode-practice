from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        prereq = defaultdict(list)
        
        for a, b in relations:
            prereq[b].append(a)
        
        
        seen = (n +1) * [0]
        
        semester = dict()
        
        counter = 0
        
        def dfsHelper(src: int) -> Tuple[Union[int, bool]]:
            """
            returns False if cycle is found
            """
            nonlocal counter, seen, semester, prereq
            seen[src] = 1
            ans = 0
            for v in prereq[src]:
                # print("src, v: ", src, v)
                # print("seen[v]: ", seen[v])
                if seen[v] == 1:
                    # Cycle detected
                    return False
                elif seen[v] == 0:
                    checkNotCyle = dfsHelper(v)
                    if not checkNotCyle:
                        return False
                ans = max(ans, semester[v])
                    
            seen[src] = 2
            semester[src] = ans + 1
            counter += 1
            
            return True
        
        
        for src in range(1, n + 1):
            if seen[src] == 0:
                counter = 1
                checkNotCyle  = dfsHelper(src)
                if not checkNotCyle:
                    return -1
        
        # print("semester: ", semester)
        return max(semester.values())
            
            
        