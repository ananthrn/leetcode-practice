class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeightsPref = list(height)
        maxHeightsPost = list(height)
        
        for j in range(1, len(height)):
            maxHeightsPref[j] = max(height[j], maxHeightsPref[j-1])
        
        for j in range(len(height) - 2, -1, -1):
            maxHeightsPost[j] = max(height[j], maxHeightsPost[j+1])
        
        
        ans = 0
        
        for ind, h in enumerate(height):
            level = min(maxHeightsPref[ind], maxHeightsPost[ind])
            # print("ind: ", ind)
            # print("level: ", level)
            # print("h: ", h)
            ans += level - h
        
        return ans
        
        