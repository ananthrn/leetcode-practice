class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a/b)
        }
        
        for token in tokens:
            # print("stack: ", stack)
            # print("token: ", token)
            if token in ops:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = ops[token](operand_1, operand_2)
                stack.append(result)
            else:
                stack.append(int(token))
            
            # print("stack after:", stack)
        return stack[0]
                