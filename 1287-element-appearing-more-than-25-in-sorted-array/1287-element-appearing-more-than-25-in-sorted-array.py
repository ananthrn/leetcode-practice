class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        n = len(arr)
        
        for k, val in cnt.items():
            if val * 4 > n:
                return k
        
        return -1