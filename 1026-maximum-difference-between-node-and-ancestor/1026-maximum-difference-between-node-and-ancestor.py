# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxHelper(root, minAncestorVal, maxAncestorVal) -> int:
            if root is None:
                return 0

            thisMax = max(abs(root.val - minAncestorVal), abs(root.val - maxAncestorVal) )
            leftMax = maxHelper(root.left, min(minAncestorVal, root.val), max(root.val, maxAncestorVal))
            rightMax = maxHelper(root.right, min(minAncestorVal, root.val), max(root.val, maxAncestorVal))

            return max(thisMax, leftMax, rightMax)
        
        if root is None:
            return 0
            
        return maxHelper(root, root.val, root.val)