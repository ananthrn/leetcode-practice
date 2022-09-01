# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def traverse(rootNode: TreeNode, maxSoFar):
            nonlocal goodNodes
            if not rootNode:
                return
            
            if rootNode.val >= maxSoFar:
                goodNodes += 1
            
            newMax = max(maxSoFar, rootNode.val)
            traverse(rootNode.left, newMax)
            traverse(rootNode.right, newMax)
        
        traverse(root, - int(10**5))
        
        return goodNodes
        