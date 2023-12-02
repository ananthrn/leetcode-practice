import sortedcontainers
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sortedList = sortedcontainers.SortedList()
        
        left, right = 0, 0
        
        maxSize = 1
        
        sortedList.add(nums[0])
        
        while right < len(nums):
            currentSize = len(sortedList)
            currentDiff = sortedList[-1] - sortedList[0]
            if currentDiff <= limit:
                maxSize = max(maxSize, currentSize)
                right += 1
                if right < len(nums):
                    sortedList.add(nums[right])
            else:
                sortedList.remove(nums[left])
                left += 1
        
        
                
        
        
        return maxSize
            
            