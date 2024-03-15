class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefSums = (len(nums) + 1) * [0]
        
        for ind in range(1, len(prefSums)):
            prefSums[ind] = prefSums[ind - 1] + nums[ind - 1]
            
        
        def binSearchLowestHighest(start, end, sm):
            lowestIndex = end + 1
            left, right = start, end
            
            while left <= right:
                # print("left, righ")
                mid = (left + right)//2
                if prefSums[mid] == sm:
                    lowestIndex = min(lowestIndex, mid)
                    right = mid - 1
                elif prefSums[mid] > sm:
                    right = mid - 1
                elif prefSums[mid] < sm:
                    left = mid + 1
            
            highestIndex = start - 1
            left, right = start, end
            
            while left <= right:
                mid = (left + right)//2
                if prefSums[mid] == sm:
                    highestIndex = max(highestIndex, mid)
                    left = mid + 1
                elif prefSums[mid] > sm:
                    right = mid - 1
                elif prefSums[mid] < sm:
                    left = mid + 1
            
            return max(0, highestIndex - lowestIndex + 1)
        
        ans = 0
        cnt = collections.Counter()
        
#         for ind in range(1, len(prefSums)):
#             prefSum = prefSums[ind]
#             if goal <= prefSum:
#                 remainingSum = prefSum - goal
#                 length = binSearchLowestHighest(0, ind - 1, remainingSum)
                
#                 ans += length
        
        for prefSum in prefSums:
            remSum = prefSum - goal
            ans += cnt[remSum]
            cnt[prefSum] += 1
        return ans
            
            
                    
            