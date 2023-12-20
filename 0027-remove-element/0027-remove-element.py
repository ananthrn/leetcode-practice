class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        currentIndex = n - 1
        
        while currentIndex >=0 and nums[currentIndex] == val:
            currentIndex -= 1
        
        startIndex = 0
        
        while startIndex <= currentIndex:
            if nums[startIndex] == val:
                nums[startIndex], nums[currentIndex] = nums[currentIndex], nums[startIndex]
                while currentIndex >=startIndex and nums[currentIndex] == val:
                    currentIndex -= 1
                
            startIndex +=1
        
        return currentIndex + 1
        