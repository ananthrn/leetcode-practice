class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        numsLeftToDelete = k
        for digit in num:
            while numsLeftToDelete > 0 and numStack and numStack[-1] > digit:
                numStack.pop()
                numsLeftToDelete -=1
            numStack.append(digit)
        
        
        finalStack =  numStack[:-numsLeftToDelete] if numsLeftToDelete else numStack
        
        return "".join(finalStack).lstrip("0") or "0"
        # return helper(0, k).lstrip("0")
        
        