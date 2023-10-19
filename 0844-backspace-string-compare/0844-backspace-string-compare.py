class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getEquivalentText(string: str) -> str:
            stack = []
            
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            
            return "".join(stack)
        
        return getEquivalentText(s) == getEquivalentText(t)
        