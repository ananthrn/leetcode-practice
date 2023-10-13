class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        leftIndex = min([i for i in range(len(nums)) if nums[i] != sorted_nums[i]], default=n)
        rightIndex = max([i for i in range(len(nums)) if nums[i] != sorted_nums[i]], default=-1)
        
        # print("maxLeft, minRight", maxLeft, minRight )
        return max(0, rightIndex - leftIndex + 1)
        