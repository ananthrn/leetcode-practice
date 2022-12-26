class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastPos = n - 1
        
        for j in range(n -1 , -1, -1):
            if j + nums[j] >= lastPos:
                lastPos = j
        
        return lastPos == 0 
        