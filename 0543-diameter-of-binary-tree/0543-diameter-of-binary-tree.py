# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(srcNode: Optional[TreeNode]) -> Tuple[int]:
            
            if srcNode is None:
                return -1, -1
            
            leftDiameter, leftHeight = helper(srcNode.left)
            rightDiameter, rightHeight = helper(srcNode.right)
            
            return max(leftDiameter, rightDiameter, leftHeight + rightHeight + 2), 1 + max(leftHeight, rightHeight)
        
        diameter, height = helper(root)
        
        return diameter
        