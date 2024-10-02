class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestElems = sorted(arr, key = lambda val: abs(x - val))[:k]
        
        return sorted(closestElems)