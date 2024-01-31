class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        ans =  [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            # print(stack)
            while stack and stack[-1][0] < temp:
                popTemp, popIndex = stack.pop()
                ans[popIndex] = index - popIndex
                    
            stack.append((temp, index))
                
                
        
        return ans