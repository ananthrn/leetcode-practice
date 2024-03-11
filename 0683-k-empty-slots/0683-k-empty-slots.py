import sortedcontainers
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        
        n = len(bulbs)
        sortedBulbs = sortedcontainers.SortedList([0, n + 1])
        
        for day, bulb in enumerate(bulbs):
            index = sortedBulbs.bisect_left(bulb)
            # print("bulb: ", bulb)
            # print("sortedBulbs: ", sortedBulbs)
            # print("index: ", index)
            leftGap = -1 if index - 1 == 0 else (bulb - sortedBulbs[index - 1] - 1)
            rightGap = -1 if index == len(sortedBulbs) - 1 else (sortedBulbs[index] - bulb - 1)
            
            if k in (leftGap, rightGap):
                return day + 1
            
            sortedBulbs.add(bulb)
        
        return -1
        