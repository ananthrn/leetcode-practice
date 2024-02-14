class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIndex = 0
        negIndex = 1
        
        array = len(nums) * [None]
        
        for index, val in enumerate(nums):
            if val > 0:
                array[posIndex] = val
                posIndex+=2
            else:
                array[negIndex] = val
                negIndex += 2
        
        return array