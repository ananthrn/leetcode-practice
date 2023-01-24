class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vals = len(nums) * [None]
        
        k = k % len(nums)
#         nums = []
        
#         nums = list(nums[-k:] + nums[:len(nums) - k])
        # nums = []
        # for ind in range(len(nums)):
        #     vals[ind] = nums[(ind - k + len(nums))% len(nums)]
        # for ind in range(len(nums)):
        #     nums[ind] = vals[ind]
            
        # print("vals: ", vals)
        # nums = vals
        dummyList = list(nums[-k:] + nums[:len(nums) - k])
        print("dummyList:", dummyList)
        for ind in range(len(nums)):
            nums[ind] = dummyList[ind]
        
        
        