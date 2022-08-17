class Solution:
    def maxArea(self, height: List[int]) -> int:
        stack = []
        
        maxArea = 0
        
        start = 0
        end = len(height) - 1
        
        while start < end:
            maxArea = max(maxArea, min(height[start], height[end]) * (end - start))
            
            if height[start] >= height[end]:
                end-=1
            else:
                start+=1
        
        return maxArea
            
                
            
        