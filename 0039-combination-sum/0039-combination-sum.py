class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(targetSum: int, index: int):
            if index >= len(candidates) or targetSum < 0:
                return []
            
            thisSubsets = []
            
            for numCandidates in range(0, targetSum//candidates[index] + 1):
                if numCandidates * candidates[index] == targetSum:
                    thisSubsets.append(numCandidates * [candidates[index]])
                else:
                    nextSubsets = backtrack(targetSum - numCandidates * candidates[index], index + 1)

                    for subset in nextSubsets:
                        thisSubsets.append(numCandidates * [candidates[index]] + list(subset))
            
            return thisSubsets
            
        
        ans = backtrack(target, 0)
        
        return ans
            