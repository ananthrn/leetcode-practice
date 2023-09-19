class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appeared = set()
        
        for num in nums:
            if num in appeared:
                return num
            appeared.add(num)
        
        return -1
        