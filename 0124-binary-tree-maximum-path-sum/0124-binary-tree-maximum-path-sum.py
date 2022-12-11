# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -2000
        
        def helper(root: TreeNode) -> int:
            nonlocal maxPath
            if root is None:
                return 0
            
            leftBest = helper(root.left)
            rightBest = helper(root.right)
            
            bestPath = root.val + max(0, leftBest) + max(0, rightBest)
            
            maxPath = max(maxPath, bestPath)
            return max(0, leftBest, rightBest) + root.val
        
        
        helper(root)
        
        return maxPath