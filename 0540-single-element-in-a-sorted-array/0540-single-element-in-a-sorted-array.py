class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        
        start, end = 1, len(nums) - 2

        while start <= end:
            mid = (start + end)//2

            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif nums[mid] == nums[mid-1]:
                if mid%2 == 1:
                    # the single element is to the right
                    start = mid + 1
                else:
                    # single element is to the left
                    end = mid - 1
            elif nums[mid] == nums[mid+1]:
                if mid%2 == 0:
                    # single element is to the right
                    start = mid + 1
                else:
                    end = mid - 1
        

        return -1



