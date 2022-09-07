# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        s = ""
        def helper(rootNode):
            nonlocal s
            s += '('
            if rootNode is not None:
                s += str(rootNode.val)
                
                if rootNode.left is None and rootNode.right is None:
                    pass
                elif rootNode.left is None and rootNode.right is not None:
                    helper(rootNode.left)
                    helper(rootNode.right)
                elif rootNode.left is not None and rootNode.right is None:
                    helper(rootNode.left)
                elif rootNode.left is not None and rootNode.right is not None:
                    helper(rootNode.left)
                    helper(rootNode.right)
                    
            s += ')'
        
        helper(root)
        
        return s[1:-1]
        