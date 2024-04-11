class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        numToDelete = k
        for digit in num:
            while numToDelete > 0 and numStack and numStack[-1] > digit:
                numStack.pop()
                numToDelete -= 1
            numStack.append(digit)
        
        finalStack = numStack if numToDelete == 0 else numStack[:-numToDelete]
        
        return "".join(finalStack).lstrip("0") or "0"
            
        