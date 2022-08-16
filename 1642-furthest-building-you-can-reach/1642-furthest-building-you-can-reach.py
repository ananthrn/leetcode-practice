from sortedcontainers import SortedList
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        ladderSet = SortedList()
        for ind in range(len(heights) - 1):
            currentHeight = heights[ind]
            nextHeight = heights[ind + 1]
            
            climb = nextHeight - currentHeight
            
            if climb <= 0 :
                continue
            else:
                # 
                if len(ladderSet) < ladders:
                    ladderSet.add(climb)
                else:
                    
                    if ladders == 0 or climb <= ladderSet[0]:
                        # climb is lower than the lowest climb so far
                        # use bricks
                        bricks -= climb
                    else:
                        # use a ladder for this one and replace another ladder
                        # with bricks
                        replacedClimb = ladderSet.pop(0)
                        ladderSet.add(climb)
                        bricks -= replacedClimb
                
                if bricks < 0:
                    return ind
                    
        
        return len(heights) - 1
        