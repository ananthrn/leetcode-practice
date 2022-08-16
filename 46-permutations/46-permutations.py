from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = set()
        seen = len(nums) * [False]
        perm = []
        def backtrack():
            if len(perm) == len(nums):
                permutations.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if not seen[i]:
                    perm.append(nums[i])
                    seen[i] = True
                    backtrack()
                    seen[i] = False
                    perm.pop()
                    
        backtrack()
        
        return list(permutations)
        
        
        