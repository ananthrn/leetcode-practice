class Solution:
    def minimizeResult(self, expression: str) -> str:
        plusIndex = expression.index('+')
        bestVal = int(expression[0:plusIndex]) + int(expression[plusIndex+1:])
        bestString = "(" + expression + ")"
        
        for firstIndex in range(plusIndex):
            for secondIndex in range(plusIndex+1, len(expression)):
                leftStr = expression[:firstIndex]
                midStr = expression[firstIndex:secondIndex+1]
                rightStr = expression[secondIndex + 1:]
                leftVal = 1 if len(leftStr) == 0 else int(leftStr)
                
                midVal = int(expression[firstIndex:plusIndex]) + int(expression[plusIndex + 1: secondIndex + 1])
                rightVal = 1 if len(rightStr) == 0 else int(rightStr)
                
                value = leftVal * midVal * rightVal
                
                if value < bestVal:
                    bestVal = value
                    bestString = leftStr + "(" + midStr + ")" + rightStr
                
        
        return bestString
        