class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0 
        
        minSoFar = arrays[0][0]
        maxSoFar = arrays[0][-1]
        
        for array in arrays[1:]:
            newMin = array[0]
            newMax = array[-1]
            
            res = max(
                res,
                abs(newMin - maxSoFar),
                abs(newMax - minSoFar),
            )
            
            minSoFar = min(minSoFar, newMin)
            maxSoFar = max(maxSoFar, newMax)
                
        return res
        