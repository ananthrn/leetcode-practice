class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        degree = cnt.most_common()[0][1]
        
        left = 0
        right = 0
        
        bestLength = len(nums)
        currentCounter = collections.Counter(nums[0:1])
        
        while left <= right and right < len(nums):
            currentDegree = currentCounter.most_common()[0][1]
            if currentDegree == degree:
                bestLength = min(bestLength, right - left + 1)
                currentCounter[nums[left]] -= 1
                left += 1
            else:
                right += 1
                if right < len(nums):
                    currentCounter[nums[right]] += 1
                
                
        
        return bestLength
        
        
        