# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val in (0, 1):
            return root.val == 1
        
        funcMap = {
            2: lambda x, y:  x or y,
            3: lambda x, y:  x and y
        }
    
        return funcMap[root.val](
            self.evaluateTree(root.left), 
            self. evaluateTree(root.right)
        )
        