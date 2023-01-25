from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        start = 0
        end = k - 1
        
        sl = SortedList(nums[:k])
        ans = []
        while end < n:
            ans.append(sl[-1])
            sl.remove(nums[start])
            start += 1
            end += 1
            if end < n:
                sl.add(nums[end])
        
        return ans
        
        