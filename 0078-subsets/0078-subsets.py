class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(index: int):
            if index >= len(nums):
                return [[]]
            
            nextSubsets = backtrack(index + 1)
            
            thisSubsets = []
            
            for subset in nextSubsets:
                thisSubsets.append(list(subset) + [nums[index]])
                thisSubsets.append(list(subset))
            
            return thisSubsets 
        
        ans = backtrack(0)
        
        return ans