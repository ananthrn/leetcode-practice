class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        if len(nums) < 4:
            return 0
        
        n = len(nums)
        
        minDiff = nums[-1] - nums[0]
        
        for i in range(4):
            minDiff = min(minDiff, nums[n - 4 + i] - nums[i])
        
        return minDiff