import sortedcontainers
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        @lru_cache(None)
        def getNumSessions(tasksRemaining: Set[int], remainingTime: int) -> int:
            if len(tasksRemaining) == 0:
                return 0
            
            ans = len(tasks)
            for taskIndex in tasksRemaining:
                if tasks[taskIndex] <= remainingTime:
                    ans = min(ans, getNumSessions(tasksRemaining - {taskIndex}, remainingTime - tasks[taskIndex]))
                else:
                    ans = min(ans, 1 + getNumSessions(tasksRemaining - {taskIndex}, sessionTime - tasks[taskIndex]))
            
            return ans
        
        numSessions = getNumSessions(frozenset(range(len(tasks))), sessionTime)
        
        return numSessions + 1
            
            
        