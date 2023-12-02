class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        taskIndex = 0
        n = len(tasks)
        day = 0
        
        nextDayPossible = dict()
        
        for taskIndex, taskNumber in enumerate(tasks):
            day = max(nextDayPossible.get(taskNumber, -1), day + 1)
            
            # print("taskIndex, taskNumber, day: ", taskIndex, taskNumber, day)
            nextDayPossible[taskNumber] = day + space + 1
        
        
        return day