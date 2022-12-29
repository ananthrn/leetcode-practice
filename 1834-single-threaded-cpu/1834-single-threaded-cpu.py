
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([task[0], ind, task[1]] for ind, task in enumerate(tasks))
        
        
        
        taskOrder = []
        
        
        currentTime = tasks[0][0]
        taskIndex = 0
        
        taskHeap = []
        
        while taskIndex < len(tasks) or len(taskHeap) > 0:
            # if task heap is empty, move currentTime
            if len(taskHeap) == 0:
                currentTime = max(currentTime, tasks[taskIndex][0])
            # Add tasks to minHeap that started on or before currentTime
            while taskIndex < len(tasks) and tasks[taskIndex][0] <= currentTime:
                heapq.heappush(taskHeap, (tasks[taskIndex][2], tasks[taskIndex][1]))
                taskIndex += 1
                
            # Retrieve task with min processingTime
            bestProcessTime, bestIndex = heapq.heappop(taskHeap)
            # process task
            taskOrder.append(bestIndex)
            # update currentTime to be currentTime plus processTime
            currentTime = currentTime + bestProcessTime
            
            
        
        return taskOrder
        
            
        