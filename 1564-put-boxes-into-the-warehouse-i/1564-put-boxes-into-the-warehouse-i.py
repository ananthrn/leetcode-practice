class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes = sorted(boxes)
        
        lastPos = len(warehouse) - 1
        
        boxesFit = 0
        
        prefixMin = list(warehouse)
        
        for ind in range(1, len(prefixMin)):
            prefixMin[ind] = min(prefixMin[ind], prefixMin[ind - 1])
        
        assignment = collections.defaultdict(int)
        for box in boxes:
            if lastPos < 0:
                return boxesFit
            
            while lastPos >= 0 and prefixMin[lastPos] < box:
                lastPos -=1
            
            if lastPos < 0:
                return boxesFit
            
            assignment[lastPos] = box
            boxesFit += 1
            lastPos -= 1
            # print("boxesFit: ", boxesFit)
            # print("assignment: ", assignment)
        
        return boxesFit
                
            
        