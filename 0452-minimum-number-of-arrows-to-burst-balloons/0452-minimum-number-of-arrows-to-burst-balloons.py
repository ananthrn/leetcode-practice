class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        events = []
        
        for index, (left, right) in enumerate(points):
            events.append(
                (left, 0, index)
            )
            
            events.append(
                (right, 1, index)
            )
        
        events = sorted(events)
        
        
        arrowsNeeded = 0
        
        indexSet = set()
        for coordinate, isEnd, index in events:
            if isEnd == 0:
                indexSet.add(index)
            else:
                if index in indexSet:
                    arrowsNeeded += 1
                    indexSet = set()
            # print("coordinate, isEnd, index: ", coordinate, isEnd, index)
            # print("indexSet: ", indexSet)
            # print("arrowsNeeded: ", arrowsNeeded)
            # print()
        return arrowsNeeded
        
        