# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        overAllAnswer = 0
        
        def helper(src: Optional[TreeNode]) -> int:
            nonlocal overAllAnswer
            if src is None:
                return 0
            
            descSum = helper(src.left) + helper(src.right)
            
            if descSum == src.val:
                overAllAnswer += 1
            
            return descSum + src.val 
        
        helper(root)
        
        return overAllAnswer
        