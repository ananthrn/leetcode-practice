from collections import Counter
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        sortedItems = sorted(c.items(), key = lambda x: x[0])
        
        currentMax = sortedItems[0][0] - 1
        ans = 0
        for key, cnt in sortedItems:
            
            # print("key, cnt:", key, cnt)
            # print("currentMax: ", currentMax)
            moves = (cnt) * max(0, currentMax + 1 - key) + ((cnt) * (cnt-1))//2
            ans += moves
            # print("moves: ", moves)
            # print("ans: ", ans)
            # print()
            currentMax = max(key, max(currentMax + 1, key) + cnt - 1)
        
        return ans
            
        