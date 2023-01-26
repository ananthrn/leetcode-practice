class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)
        
        return list(filter(lambda key: cnt[key] > n//3, cnt.keys()))
        