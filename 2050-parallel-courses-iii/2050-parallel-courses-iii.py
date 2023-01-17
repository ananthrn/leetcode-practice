class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        def helper(src: int) -> int:
            if months[src] is not None:
                return months[src]
            
            
            prevMonthsNeeded = 0
            
            for prereq in adj[src]:
                prevMonths = helper(prereq)
                prevMonthsNeeded = max(prevMonthsNeeded, prevMonths)
            
            months[src] = time[src] + prevMonthsNeeded
            print("src: ", src)
            print("months[src]: ", months[src])
            print("prevMonthsNeeded: ", prevMonthsNeeded)
            return months[src]
            
        
        months = n * [None]
        adj = collections.defaultdict(list)
        
        for prereq, nxtCourse in relations:
            adj[nxtCourse - 1].append(prereq - 1)
        
        for course in range(n):
            if months[course] is None:
                helper(course)
        
        print("months: ", months)
        return max(months, default=0)
            
        