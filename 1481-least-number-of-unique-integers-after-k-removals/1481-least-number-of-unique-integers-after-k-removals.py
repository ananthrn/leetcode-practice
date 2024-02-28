class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        
        totalDiff = len(cnt.keys())
        
        sortedVals = sorted(cnt.values())
        
        for ind, val in enumerate(sortedVals):
            if k >= val:
                k -= val
            else:
                return totalDiff - ind
        
        return 0