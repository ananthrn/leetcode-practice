class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        sign = lambda a: -1 if a < 0 else 1
        
        opMap = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: sign(a) * sign(b) * (abs(a) // abs(b)),
        }
        
        stack = []
        
        for token in tokens:
            if token in opMap:
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                stack.append(opMap[token](operand2, operand1))
                
#                 print("token: ", token)
                
#                 print(f"result of {operand2} {token} {operand1}:", opMap[token](operand2, operand1))
            else:
                stack.append(int(token))
            
            # print("stack: ", stack)
        
        return stack[-1]