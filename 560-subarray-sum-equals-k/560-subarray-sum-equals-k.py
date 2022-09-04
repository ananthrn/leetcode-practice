class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSums = list(nums)
        
        for ind  in range(1, len(nums)):
            prefSums[ind] += prefSums[ind - 1]
            
        sumsSeen = {0: 1}
        
        ans = 0
        for ind, prefSum in enumerate(prefSums):
            ans += sumsSeen.get(prefSum - k, 0)
            sumsSeen[prefSum] = sumsSeen.get(prefSum, 0) + 1
        
        return ans
        