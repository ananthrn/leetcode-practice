class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        
        numToIndex = {
            num: index for index, num in enumerate(arr2)
        }
        
        return sorted(arr1, key=lambda x: (numToIndex.get(x, 1000000), x) )
        