# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def helper(node: TreeNode) -> Tuple[int]:
            """
            returns sum of node vals, total number of node vals, number of node vals == average of subtree
            """
            if node is None:
                return 0, 0, 0
            
            leftSum, leftNum, leftAns = helper(node.left)
            rightSum, rightNum, rightAns = helper(node.right)
            
            thisSum, thisNum = leftSum + rightSum + node.val, leftNum + rightNum + 1
            
            thisAns = leftAns + rightAns + (1 if thisSum//thisNum == node.val else 0)
            
            return thisSum, thisNum, thisAns
        
        
        rootSum, rootNum, rootAns = helper(root)
        
        return rootAns
        