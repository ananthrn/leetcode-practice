from sortedcontainers import SortedList
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        diffs = SortedList()
        ans = 0
        for j in range(n):
            currentDiff =  nums1[j] - nums2[j]
            
            bestIndex = diffs.bisect_right(-currentDiff)
            
            # print("j: ", j)
            # print("-currentDiff: ", -currentDiff)
            # print("diffs: ", diffs)
            # print("bestIndex: ", bestIndex)
            # print("Satisfying indices: ", len(diffs) - bestIndex)
            # print()
            if len(diffs) > 0:
                ans += len(diffs) - bestIndex
            
            diffs.add(currentDiff)
        
            
        return ans
        