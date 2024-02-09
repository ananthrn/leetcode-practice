class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(index) -> List[int]:
            if index >= len(nums):
                return []
            
            bestNext = []
            
            for nextIndex in range(index+1, len(nums)):
                if nums[nextIndex] % nums[index] == 0:
                    valNext = helper(nextIndex)
                    if len(valNext) > len(bestNext):
                        bestNext = valNext
                
            return [nums[index]] + bestNext
            
        
        nums = sorted(nums)
        
        bestVal = []
        
        for index in range(0, len(nums)):
            valNext = helper(index)
            if len(valNext) > len(bestVal):
                bestVal = valNext
                
        return bestVal