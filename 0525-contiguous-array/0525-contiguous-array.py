class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        firstIndexOfCount = dict()
        
        firstIndexOfCount[0] = -1
        
        ans = 0
        currentCount = 0
        for index, num in enumerate(nums):
            currentCount += (-1 if num == 0 else 1)
            
            # print("index, num, currentCount: ", index, num, currentCount)
            if currentCount in firstIndexOfCount:
                ans = max(ans, index - firstIndexOfCount[currentCount])
            else:
                firstIndexOfCount[currentCount] = index
        
        return ans
        
        