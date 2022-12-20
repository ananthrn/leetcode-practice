# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        MAX_LEN = 0
        
        def helper(rootNode: Optional[TreeNode]) -> int:
            if rootNode is None:
                return 0, 0
            
            leftVal, leftHeight = helper(rootNode.left)
            rightVal, rightHeight = helper(rootNode.right)
            
            thisHeight = 1
            thisVal = 1
            
            if rootNode.left is not None and rootNode.left.val == rootNode.val:
                thisHeight = max(1 + leftHeight, thisHeight)
                thisVal += leftHeight
                
            if rootNode.right is not None and rootNode.right.val == rootNode.val:
                thisHeight = max(1 + rightHeight, thisHeight)
                thisVal += rightHeight
            
            
            return max(thisVal, leftVal, rightVal), thisHeight
        
        rootVal, rootHeight = helper(root)
        
        return max(0, rootVal - 1)
                