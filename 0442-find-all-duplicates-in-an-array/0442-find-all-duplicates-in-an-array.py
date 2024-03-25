class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        
        return [num for num in cnt if cnt[num] == 2]
        