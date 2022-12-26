class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = collections.Counter(arr1)
        
        ans = []
        
        for val in arr2:
            ans += c[val] * [val]
            c[val] = 0
        
        for val, cnt in sorted(c.items()):
            ans += cnt * [val]
        
        return ans
        