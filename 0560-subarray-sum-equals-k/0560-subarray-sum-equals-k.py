class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSet = collections.defaultdict(int)
        
        currentSum = 0
        
        prefixSet[0] += 1
        
        ans = 0
        for num in nums:
            currentSum += num
            # prefixSet[currentSum] += 1
            ans += prefixSet[currentSum - k]
                
            prefixSet[currentSum] += 1
        
        return ans
        