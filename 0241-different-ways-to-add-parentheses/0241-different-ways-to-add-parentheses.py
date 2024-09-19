class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        funcMap = {
            "*": lambda a, b: a * b,
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
        }
        def backtrack(expr: str) -> List[int]:
            if expr.isnumeric():
                return [int(expr)]
            
            answers = []
            for index, val in enumerate(expr):
                if val in funcMap:
                    leftAnswers = backtrack(expr[:index])
                    rightAnswers = backtrack(expr[index + 1:])
                    
                    newAnswers = [
                        funcMap[val](leftAnswer, rightAnswer) for leftAnswer in leftAnswers for rightAnswer in rightAnswers
                    ]
                    
                    answers += newAnswers
            
            return answers
            
        
        return backtrack(expression)
            