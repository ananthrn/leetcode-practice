class Solution:
    def simplifyPath(self, path: str) -> str:
        vals = path.split('/')
        print(vals)
        stack = []
        
        for val in vals:
            if val not in ("", "."):
                if val == "..":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(val)
        
        return "/" + "/".join(stack)
        