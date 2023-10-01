class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left, right = 0, 0
        
        ans = 0
        for ind in range(1, len(nums)):
            if nums[ind] > nums[ind - 1]:
                right = ind
            else:
                n = right - left + 1
                ans += int((n * (n+1))/2)
                left, right = ind, ind
        n = right - left + 1
        ans += int((n * (n+1))/2)
        return ans
        