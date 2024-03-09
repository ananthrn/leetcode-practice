class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def index(a, x):
            'Locate the leftmost value exactly equal to x'
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            raise ValueError
        
        
        for num in nums1:
            try:
                ind = index(nums2, num)
                return num
            except:
                pass
        
        return -1
            