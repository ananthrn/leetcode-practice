class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        effectiveHeights = list(warehouse)
        
        minHeight = inf
        for ind in range(0, len(warehouse)):
            minHeight = min(minHeight, warehouse[ind])
            effectiveHeights[ind] = minHeight
        
        minHeight = inf
        for ind in range(len(warehouse) - 1, -1, -1):
            minHeight = min(minHeight, warehouse[ind])
            effectiveHeights[ind] = max(effectiveHeights[ind ], minHeight)
        
        print("effectiveHeights: ", effectiveHeights)
        
        effectiveHeights = sorted(effectiveHeights)
        boxes = sorted(boxes)
        
        count = 0
        boxIndex = 0
        
        for effectiveHeight in effectiveHeights:
            if boxIndex < len(boxes) and boxes[boxIndex] <= effectiveHeight:
                count += 1
                boxIndex += 1
        
        return count