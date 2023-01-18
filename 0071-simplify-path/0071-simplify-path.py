class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        
        stack = []
        
        for val in paths:
            
            if val == ".":
                pass
            elif val == "..":
                if len(stack) > 0:
                    stack.pop()
            elif val != "":
                stack.append(val)
        
        ans = "/".join(stack)
        
        return "/" + ans
                
                
                
        
        