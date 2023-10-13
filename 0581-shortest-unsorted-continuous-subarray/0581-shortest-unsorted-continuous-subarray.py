class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return 0
        
        prefixMax = n * [0]
        prefixMin =  n * [0]
        suffixMax = n * [0]
        suffixMin = n * [0]
        
        prefixMax[0] = nums[0]
        prefixMin[0] = nums[0]
        
        for j in range(1, n):
            prefixMax[j] = max(prefixMax[j-1], nums[j])
            prefixMin[j] = min(prefixMin[j-1], nums[j])
        
        
        suffixMax[-1] = nums[-1]
        suffixMin[-1] = nums[-1]
        
        for j in reversed(range(0, n - 1)):
            suffixMax[j] = max(suffixMax[j + 1], nums[j])
            suffixMin[j] = min(suffixMin[ j + 1], nums[j])
        
        
        maxLeft = -1
        
        for j in range(0, n):
            maxLeft = j
            if j < n - 1 and prefixMax[j] > suffixMin[j + 1]:
                break
        
        
        minRight = n
        
        for j in reversed(range(0, n)):
            minRight = j
            if j > 0 and suffixMin[j] < prefixMax[j - 1]:
                break
        
        # print("maxLeft, minRight", maxLeft, minRight )
        return max(0, minRight - maxLeft + 1)
        