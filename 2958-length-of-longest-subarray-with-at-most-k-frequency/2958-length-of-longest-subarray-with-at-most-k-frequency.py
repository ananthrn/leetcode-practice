class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        
        left, right = 0, -1
        
        ans = 0
        
        for right in range (len(nums)):
            counter[nums[right]] += 1
            
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
        