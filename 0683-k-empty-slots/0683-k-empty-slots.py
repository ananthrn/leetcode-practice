from sortedcontainers import SortedList
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        sl = SortedList()
        n = len(bulbs)
        
        for day, bulb in enumerate(bulbs):
            sl.add(bulb)
            indexAdded = sl.index(bulb)
            
            if indexAdded > 0 and bulb - sl[indexAdded - 1] == k + 1:
                return day + 1
            
            if indexAdded < len(sl) - 1 and sl[indexAdded + 1] - bulb == k + 1:
                return day + 1
        
        return -1
            
        