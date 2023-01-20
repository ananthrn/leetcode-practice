class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(index: int) -> List[int]:
            ans = [[nums[index]]]
            
            for nextIndex in range(index + 1, len(nums)):
                if nums[nextIndex] >= nums[index]:
                    nextAns = helper(nextIndex)
                    
                    for nextSeq in nextAns:
                        ans.append([nums[index]] + nextSeq)
            
            return ans
            
        ans = []
        
        for index in range(0, len(nums)):
            ans += helper(index)
            
        filteredAns = list(filter(lambda val : len(val) >=2, ans))
        
        finalAns = set()
        
        for seq in filteredAns:
            finalAns.add(tuple(seq))
            
        return finalAns
    