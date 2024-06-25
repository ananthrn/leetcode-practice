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
        
        
        effectiveHeights = sorted(effectiveHeights)
        boxes = sorted(boxes)
        
        print("effectiveHeights: ", effectiveHeights)
        print("boxes: ", boxes)
#         count = 0
#         boxIndex = 0
        
#         # go by effectiveHeight order
#         for effectiveHeight in effectiveHeights:
#             if boxIndex < len(boxes) and boxes[boxIndex] <= effectiveHeight:
#                 count += 1
#                 boxIndex += 1
        
        count = 0
        heightIndex = 0
        # go by box order
        for box in boxes:
            while heightIndex < len(effectiveHeights) and box > effectiveHeights[heightIndex]:
                heightIndex += 1
            
            if heightIndex < len(effectiveHeights):
                count += 1
                heightIndex += 1
        
        return count
            