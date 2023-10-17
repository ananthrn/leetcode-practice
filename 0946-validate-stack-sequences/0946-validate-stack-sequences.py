class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popIndex = 0
        for pushedElem in pushed:
            stack.append(pushedElem)
            
            while popIndex < len(popped) and stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1
        
        return popIndex == len(pushed)
        