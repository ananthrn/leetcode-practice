class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        
        if all(nums[startIndex + 2] - nums[startIndex] <= k for startIndex in range(0, len(nums), 3)):
            return [nums[startIndex: startIndex + 3] for startIndex in range(0, len(nums), 3)]
        else:
            return []