class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end)//2
            
            print("start, mid, end: ", start, mid, end)
            print("nums[start], nums[mid], nums[end]: ", nums[start], nums[mid], nums[end])
            if nums[mid] == target:
                return mid
            
            elif nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1