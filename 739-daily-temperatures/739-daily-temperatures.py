from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        n = len(temperatures)
        ans = n * [0]
        for ind  in range(n - 1, -1, -1):
            temp = temperatures[ind]
            while not len(stack) == 0 and stack[-1][0] <= temp:
                stack.pop()
            
            if not len(stack) == 0:
                ans[ind] = stack[-1][1] - ind
            
            stack.append((temp, ind))
        
        return ans
        