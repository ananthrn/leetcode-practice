class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(ind, cur):
            if len(cur) >= 2:
                ans.add(tuple(cur))
            
            for nxtInd in range(ind + 1, len(nums)):
                if ind == -1 or nums[nxtInd] >= nums[ind]:
                    cur.append(nums[nxtInd])
                    backtrack(nxtInd, cur)
                    cur.pop()
        
        backtrack(-1, [])
        
        return list(ans)
        