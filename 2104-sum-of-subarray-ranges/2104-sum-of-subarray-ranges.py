class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        minLeft = list(range(n))
        minRight = list(range(n))
        
        maxLeft = list(range(n))
        maxRight = list(range(n))
        
        for ind in range(n):
            for j in reversed(range(ind)):
                if nums[ind] < nums[j]:
                    minLeft[ind] = j
                else:
                    break
            
            for j in reversed(range(ind)):
                if nums[ind] > nums[j]:
                    maxLeft[ind] = j
                else:
                    break
            
            for j in range(ind + 1, n):
                if nums[ind] <= nums[j]:
                    minRight[ind] = j
                else:
                    break
            
            for j in range(ind + 1, n):
                if nums[ind] >= nums[j]:
                    maxRight[ind] = j
                else:
                    break
        
#         print("minLeft: ", minLeft)
#         print("minRight: ", minRight)
        
#         print("maxLeft: ", maxLeft)
#         print("maxRight: ", maxRight)
        
        ans = 0 
        
        for ind in range(n):
            
            maxWindow = (ind - maxLeft[ind] + 1) * (maxRight[ind] - ind + 1)
            minWindow = (ind - minLeft[ind] + 1) * (minRight[ind] - ind + 1)
            thisAnswerPositive = nums[ind] * maxWindow
            thisAnswerNegative = nums[ind] * minWindow
            
            # print("ind, nums[ind]: ", ind, nums[ind])
            # print("maxWindow: ", maxWindow)
            # print("minWindow: ", minWindow)
            # print("thisAnswerPositive: ", thisAnswerPositive)
            # print("thisAnswerNegative: ", thisAnswerNegative)
            # print()
            ans += nums[ind] * ( maxWindow -  minWindow)
        
        
        
        return ans
        