class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        currentWindow = list(range(n))
        
        for i in range(n):
            j = i
            while j < n and nums[j] >= nums[i]:
                j+=1
                
            currentWindow[i] = j - 1
        
        
        return sum(currentWindow[i] - i + 1 for i in range(n))