class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            
            startIntersect = max(start1, start2)
            endIntersect = min(end1, end2)
            
            if endIntersect - startIntersect >= duration:
                return [startIntersect, startIntersect + duration]
            
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        
        return []