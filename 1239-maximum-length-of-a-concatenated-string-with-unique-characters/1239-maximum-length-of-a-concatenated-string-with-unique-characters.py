class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        @cache
        def helper(currentIndex: int, currentSet: Set[chr]) -> int:
            if currentIndex >= len(arr):
                return 0
            
            if currentIndex in ineligible or len(frozenset(arr[currentIndex]) & currentSet) > 0:
                return helper(currentIndex + 1, currentSet)
            
            return max(
                helper(currentIndex + 1, currentSet),
                len(arr[currentIndex]) + helper(currentIndex + 1, currentSet | frozenset(arr[currentIndex]))
            )
        
        ineligible = set(
            [ 
                index for index, string in enumerate(arr)
                if collections.Counter(string).most_common()[0][1] > 1
            ]
        )
        
        # print("ineligible: ", ineligible)
        ans = helper(0, frozenset())
        
        return ans
            
            
            
        