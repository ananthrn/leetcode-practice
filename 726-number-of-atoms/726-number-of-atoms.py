from collections import defaultdict, Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        count = defaultdict(int)
        stack = [Counter()]
        
        n = len(formula)
        i = 0
        
        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i+=1
            elif formula[i] == ')':
                
                top = stack.pop()
                
                i += 1
                i_start = i
                
                while i < n and formula[i].isdigit():
                    i+=1
                
                multiplicity = int(formula[i_start: i] or 1) 
                
                for name,  v in top.items():
                    stack[-1][name] += v * multiplicity
                    
            else:
                i_start = i
                i += 1
                
                while i < n and formula[i].islower(): 
                    i+=1
                
                name = formula[i_start:i]
                
                i_start = i
                
                while i < n and formula[i].isdigit():
                    i+=1
                
                multiplicity = int(formula[i_start: i] or 1) 
                
                stack[-1][name] += multiplicity
        
        
        print(stack[-1])
        ans = "".join(
            [name + (
                str(cnt) if cnt > 1 else ""
            )
             for name, cnt in sorted(stack[-1].items())
            ]
        )
        return ans
        