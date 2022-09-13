# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(root: Optional[TreeNode]):
            assert root is not None
            
            leftVal, leftAns = helper(root.left) if (root.left is not None) else (root.val, 0)
            rightVal, rightAns = helper(root.right) if (root.right is not None) else (root.val, 0)
            
            if leftVal == rightVal == root.val:
                return (root.val, leftAns + rightAns + 1)
            else:
                return (None, leftAns + rightAns)
        
        rootVal, rootAns = helper(root)
        
        return rootAns
        