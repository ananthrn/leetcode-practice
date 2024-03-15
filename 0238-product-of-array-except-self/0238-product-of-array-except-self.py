class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = list(nums)
        rightProducts = list(nums)
        
        
        for ind in range(1, len(nums)):
            leftProducts[ind] *= leftProducts[ind - 1]
            rightProducts[len(nums) - ind - 1] *= rightProducts[len(nums) - ind]
            
        ans = len(nums) * [None]
        
        for ind in range(len(ans)):
            leftProd = leftProducts[ind - 1] if ind - 1 >= 0 else 1
            rightProd = rightProducts[ind + 1] if ind + 1 < len(nums) else 1
            
            ans[ind] = leftProd * rightProd
        
        return ans
        