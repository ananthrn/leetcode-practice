class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for bitIndex in range(32):
            xorVal = 0
            for num in nums:
                currentBit = (num >> bitIndex)&1
                xorVal = xorVal ^( currentBit)
            
            if xorVal != (k >> bitIndex)&1:
                ans +=1
        
        return ans