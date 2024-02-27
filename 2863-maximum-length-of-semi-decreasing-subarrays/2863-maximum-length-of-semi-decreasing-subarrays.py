class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        stack = []
        
        for j in range(n - 1, -1, -1):
            if not stack or nums[j] < stack[-1][0]:
                stack.append((nums[j], j))
        
        currentMax = -math.inf
        
        currentAnswer = 0
        
        for i in range(n):
            if nums[i] > currentMax:
                
                currentMax = nums[i]
                
                print(f"i: {i}, nums[i]: {nums[i]}")
                print(f"Before stack: {stack}")
#                 while stack and (stack[-1][0] < nums[i] or stack[-1][1] <= i):
                    
#                     if stack[-1][0] < nums[i] and i < stack[-1][1]:
#                         currentAnswer = max(currentAnswer, stack[-1][1] - i  + 1)
                        
#                     stack.pop()
                
                stackMax = max([stack[j][1] - i  + 1 for j in range(len(stack)) if stack[j][0] < nums[i]], default=0)       
                
                currentAnswer = max(currentAnswer, stackMax)
                
                print(f"After stack: {stack}")
                print(f"stackMax: {stackMax}")
                print(f"currentAnswer: {currentAnswer}")
                print()
        
        return currentAnswer