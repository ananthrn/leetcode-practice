# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        valueFound = None
        maxDepthSeen = -1
        def helper(src: Optional[TreeNode], depth: int, leftness: int):
            nonlocal maxDepthSeen, valueFound
            
            if src is None:
                return
            
            
            
            if depth > maxDepthSeen:
                maxDepthSeen = depth
                valueFound = src.val
            
            print("Src.val, depth, leftness: ", src.val, depth, leftness)
            print("maxDepthSeen, valueFound: ", maxDepthSeen, valueFound)
            print()
            helper(src.left, depth + 1, leftness - 1)
            helper(src.right, depth + 1, leftness + 1)
        
        
        helper(root, 0, 0)
        
        return valueFound
        
        