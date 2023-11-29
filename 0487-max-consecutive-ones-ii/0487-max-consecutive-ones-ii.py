class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        @lru_cache
        def helper(index: int, canFlip: bool) -> int:
            if index >= len(nums):
                return 0
            
            if nums[index] == 1:
                return 1 + helper(index + 1, canFlip)
            
            elif nums[index] == 0:
                if canFlip:
                    return 1 + helper(index + 1, False)
                else:
                    return 0
        
        
        return max(helper(index, True) for index in range(len(nums)))
        