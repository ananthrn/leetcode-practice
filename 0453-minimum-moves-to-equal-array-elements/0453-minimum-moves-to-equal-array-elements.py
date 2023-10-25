class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mnVal = min(nums)
        
        ans = sum([val - mnVal for val in nums])
        
        return ans
        