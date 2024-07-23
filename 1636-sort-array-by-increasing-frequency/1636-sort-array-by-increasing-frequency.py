class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        
        nums = sorted(nums, key=lambda x: (cnt[x], - x))
        
        return nums