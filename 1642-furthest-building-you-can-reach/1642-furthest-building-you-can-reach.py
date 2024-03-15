class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        
        def isReachable(reachableIndex: int, bricks: int, ladders: int) -> bool:
            # nonlocal bricks, ladders
            climbs = []
            
            for index in range(reachableIndex):
                if heights[index + 1] > heights[index]:
                    climbs.append(heights[index + 1] - heights[index])
            
            # print("reachableIndex: ", reachableIndex)
            # print("climbs: ", sorted(climbs))
            # print()
            for climb in sorted(climbs):
                if bricks >= climb:
                    bricks -= climb
                elif ladders > 0:
                    ladders -= 1
                else:
                    return False
            
            return True
        
        
        
        left, right = 0, len(heights) - 1
        
        bestIndex = 0
        
        
#         canReach = {
#             index: isReachable(index, bricks, ladders) for index in range(len(heights))
#         }
        
#         print(canReach)
        
        while left <= right:
            mid = (left + right)//2
            
            if isReachable(mid, bricks, ladders):
                bestIndex = max(bestIndex, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        return bestIndex