class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        
        ans = []
        
        for key, val in counter1.items():
            if key in counter2:
                ans += min(val, counter2[key]) * [key]
        
        return ans
        