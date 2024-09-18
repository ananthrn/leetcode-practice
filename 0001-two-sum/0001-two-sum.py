class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        
        for index, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], index]
            seen[num] = index
        
        return [0, 0]