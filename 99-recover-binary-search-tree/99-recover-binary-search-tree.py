# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        values = []
        def getList( rootNode: Optional[TreeNode]) -> None:
            if rootNode:
                getList(rootNode.left)
                values.append(rootNode.val)
                getList(rootNode.right)
        
        getList(root)
        values = sorted(values, reverse=True)
        def recover(rootNode: Optional[TreeNode]) -> None:
            nonlocal values
            
            if rootNode:
                recover(rootNode.left)
                value = values.pop()
                rootNode.val = value
                recover(rootNode.right)
        
        recover(root)
            
        