class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        @lru_cache
        def helper(currentIndex: int, bricks: int, ladders: int) -> int:
            if currentIndex == len(heights) - 1:
                return currentIndex
            
            if heights[currentIndex] >= heights[currentIndex + 1]:
                return helper(currentIndex + 1, bricks, ladders)
            
            currentMax = currentIndex
            
            if ladders > 0:
                currentMax = max(
                    currentMax,
                    helper(currentIndex + 1, bricks, ladders - 1)
                )
            
            if bricks >= heights[currentIndex  + 1] - heights[currentIndex]:
                currentMax = max(
                    currentMax,
                    helper(
                        currentIndex + 1, 
                        bricks - (heights[currentIndex  + 1] - heights[currentIndex]), 
                        ladders
                    )
                )
            
            return currentMax
        
        
        currentIndex = 0
        
        climbHeap = []
        
        
        while currentIndex < len(heights) - 1:
            
            if heights[currentIndex + 1] > heights[currentIndex]:
                heightDifference = heights[currentIndex + 1] - heights[currentIndex]
                
                # print("currentIndex: ", currentIndex)
                # print("heightDifference: ", heightDifference)
                # print("climbHeap: ", climbHeap)
                # print()
                if len(climbHeap) < ladders:
                    heapq.heappush(climbHeap, heightDifference)
                elif (not climbHeap or climbHeap[0] >= heightDifference):
                    if bricks >= heightDifference:
                        bricks -= heightDifference
                    else:
                        return currentIndex
                    
                else:
                    minVal = heapq.heappop(climbHeap)
                    heapq.heappush(climbHeap, heightDifference)
                    
                    if bricks >= minVal:
                        bricks -= minVal
                    else:
                        return currentIndex
                    
                    
            
            currentIndex += 1
        
        return currentIndex
        