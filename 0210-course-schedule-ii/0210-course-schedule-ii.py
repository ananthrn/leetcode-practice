class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        
        for nxt, prereq in prerequisites:
            graph[nxt].append(prereq)
            
        courseOrder = []
        def dfsHelper(courseNum: int) -> bool:
            seen[courseNum] = 1
            for pre in graph[courseNum]:
                if seen[pre] == 1:
                    return False
                elif seen[pre] == 0:
                    check = dfsHelper(pre)
                    if not check:
                        return False
                    
            seen[courseNum] = 2
            courseOrder.append(courseNum)
            return True
        
        for courseNum in range(numCourses):
            if seen[courseNum] == 0:
                check = dfsHelper(courseNum)
                if not check:
                    return []
                
        return courseOrder
        
        
        