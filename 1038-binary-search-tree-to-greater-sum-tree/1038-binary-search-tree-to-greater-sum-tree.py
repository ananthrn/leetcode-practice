# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node: TreeNode, parentAnswer: int) -> TreeNode:
            if node is None:
                return 0
            
            
            rightSum = helper(node.right, parentAnswer)
            
            
            
            nodeAnswer = rightSum + node.val + parentAnswer
            
            leftSum = helper(node.left, nodeAnswer)
            
            subTreeSum = leftSum + rightSum + node.val
            
            node.val = nodeAnswer
            return subTreeSum
        
        helper(root, 0)
        
        return root