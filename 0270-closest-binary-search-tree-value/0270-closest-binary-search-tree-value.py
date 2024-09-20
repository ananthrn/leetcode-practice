# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        def helper(node: Optional[TreeNode]) -> None:
            nonlocal currentValue
            if node is None:
                return
            
            if (abs(target - node.val), node.val) < (abs(currentValue - target), currentValue) :
                currentValue = node.val
            
            if target == node.val:
                return
            elif target < node.val:
                helper(node.left)
            else:
                helper(node.right)
                
        currentValue = root.val
        helper(root)
        
        return currentValue