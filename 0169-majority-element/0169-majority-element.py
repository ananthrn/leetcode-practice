class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        
        return cnt.most_common()[0][0]