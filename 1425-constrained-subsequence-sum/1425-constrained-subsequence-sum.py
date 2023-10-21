import sortedcontainers
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        mxVal = n * [0]
        
        mxVal[0] = nums[0]
        
        runningMax = sortedcontainers.SortedList()
        runningMax.add(mxVal[0])
        
        for ind in range(1, n):
            mxVal[ind] = nums[ind]
            
            prevMax = runningMax[-1]
            mxVal[ind] = max(nums[ind], prevMax + nums[ind])
            
            if ind - k >= 0:
                runningMax.discard(mxVal[ind - k])
            runningMax.add(mxVal[ind])
            
#             for prevInd in range(max(0, ind - k), ind):
#                 mxVal[ind] = max(mxVal[ind], mxVal[prevInd] + nums[ind])
        
        return max(mxVal)
        