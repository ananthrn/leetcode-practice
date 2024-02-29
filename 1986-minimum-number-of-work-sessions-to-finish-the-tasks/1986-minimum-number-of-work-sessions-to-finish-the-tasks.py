import sortedcontainers
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        
        def clearBit(mask: int, bit: int) -> int:
            return ~(1 << bit) & mask
        
        def checkBitSet(mask: int, bit: int) -> bool:
            val = ((mask >> bit) & 1) 
            return val == 1
        
        @lru_cache(None)
        def getNumSessions(tasksRemaining: int, remainingTime: int) -> int:
            if tasksRemaining == 0:
                return 0
            
            # print("tasksRemaining: ", tasksRemaining)
            # print("remainingTime: ", remainingTime)
            
            ans = len(tasks)
            for taskIndex in range(0, n):
                # print(taskIndex)
                newMask = clearBit(tasksRemaining, taskIndex)
                if checkBitSet(tasksRemaining, taskIndex):
                    if remainingTime >= tasks[taskIndex]:
                        ans = min(ans, getNumSessions(newMask, remainingTime - tasks[taskIndex]))
                    else:
                        ans = min(ans, 1 + getNumSessions(newMask, sessionTime - tasks[taskIndex]))
            
            return ans
        
        n = len(tasks)
        numSessions = getNumSessions((1 << n) - 1, sessionTime)
        
        return numSessions + 1
            
            
        