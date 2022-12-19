class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        poppedIndex = 0
        pushIndex = 0
        
        n = len(pushed)
        
        currentStack = []
        
        for popElement in popped:
            if currentStack and currentStack[-1] == popElement:
                currentStack.pop()
            else:
                while pushIndex < n and pushed[pushIndex] != popElement:
                    currentStack.append(pushed[pushIndex])
                    pushIndex += 1
                
                if pushIndex == n:
                    return False
                
                pushIndex += 1
        
        return pushIndex == n
            