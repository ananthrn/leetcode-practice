class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numOnes(x: int) -> int:
            numOne = 0
            while x > 0:
                numOne += (x%2)
                x = x//2
            return numOne
        
        return sorted(arr, key=lambda x: (numOnes(x), x))