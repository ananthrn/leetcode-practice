# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root, leaves):
            if root is None:
                return 
                
            if root is not None and root.left is None and root.right is None:
                leaves.append(root.val)
                return 
            
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)
        
        leavesOne = []
        leavesTwo = []

        getLeaves(root1, leavesOne)
        getLeaves(root2, leavesTwo)

        return leavesOne == leavesTwo