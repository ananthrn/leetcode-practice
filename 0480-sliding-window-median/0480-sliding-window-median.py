import sortedcontainers
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        def getMedian(l) -> float:
            n = len(l)
            if n % 2 == 0:
                return (l[n//2] + l[n//2 - 1])/2.0
            else:
                return l[n//2]
            
        sortedlist = sortedcontainers.SortedList(nums[:k])
        
        medians = [getMedian(sortedlist)]
        
        for i in range(k, len(nums)):
            index = sortedlist.index(nums[i - k])
            sortedlist.pop(index)
            
            sortedlist.add(nums[i])
            
            medians.append(getMedian(sortedlist))
        
        return medians