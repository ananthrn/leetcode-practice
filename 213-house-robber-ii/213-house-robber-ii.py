class Solution:
    def robHelper(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = n * [0]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for j in range(2, n):
            dp[j] = max(nums[j] + dp[j-2], dp[j-1])
        
        return dp[n-1]
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.robHelper(nums[0:n-1]), self.robHelper(nums[1:]))
        