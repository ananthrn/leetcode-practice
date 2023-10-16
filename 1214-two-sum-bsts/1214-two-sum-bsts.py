# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def searchVal(node: Optional[TreeNode], val: int) -> bool:
            if not node:
                return False
            
            if node.val == val:
                return True
            elif val < node.val:
                return searchVal(node.left, val)
            else:
                return searchVal(node.right, val)
        
        def searchTarget(node: Optional[TreeNode], target: int) -> bool:
            if not node:
                return False
            
            return searchVal(root2, target - node.val) or searchTarget(node.left, target) or searchTarget(node.right, target)
        
        return searchTarget(root1, target)
        