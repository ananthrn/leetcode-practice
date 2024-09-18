class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        minPrefSum = dict()
        currentSum = 0
        
        bestSum = -math.inf 
        
        for val in nums:
            if val in minPrefSum:
                minPrefSum[val] = min(minPrefSum[val], currentSum)
            else:
                minPrefSum[val] = currentSum
            currentSum += val
            
            if val + k in minPrefSum:
                bestSum = max(bestSum, currentSum - minPrefSum[val + k])
            
            if val - k in minPrefSum:
                bestSum = max(bestSum, currentSum - minPrefSum[val - k])            
            
            
            
        
        return bestSum if bestSum > -math.inf else 0 