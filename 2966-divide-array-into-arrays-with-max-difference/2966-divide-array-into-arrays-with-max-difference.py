class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        
        ans = []
        for startIndex in range(0, len(nums), 3):
            if nums[startIndex + 2] - nums[startIndex] <= k:
                ans.append(nums[startIndex:startIndex + 3])
            else:
                return []
        
        return ans