class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        
        uniqueKey = max(filter(lambda x: cnt[x] == 1, cnt.keys()), default=-1)
        
        return uniqueKey