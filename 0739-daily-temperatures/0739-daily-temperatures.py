from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        n = len(temperatures)
        ans = n * [0]
        
        # keep a stack of decreasing temperatures
        
        for ind, temp in enumerate(temperatures):
            if not stack:
                stack.append([ind, temp])
            else:
                while stack and stack[-1][1] < temp:
                    prevIndex, prevTemp = stack.pop()
                    ans[prevIndex] = ind - prevIndex
                stack.append([ind, temp])
        
        return ans
        