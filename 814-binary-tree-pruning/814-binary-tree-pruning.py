# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfsHelper(rootNode: Optional[TreeNode]) -> int:
            if not rootNode:
                return 0
            
            leftVal = dfsHelper(rootNode.left)
            rightVal = dfsHelper(rootNode.right)
            
            if leftVal == 0:
                rootNode.left = None
            
            if rightVal == 0:
                rootNode.right = None
                
            return rootNode.val + leftVal + rightVal
        
        rootVal = dfsHelper(root)
        
        return root if rootVal > 0 else None
        