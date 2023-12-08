# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxAvg = 0.0
        def helper(node: Optional[TreeNode]):
            nonlocal maxAvg
            if node is None:
                return 0.0, 0, 0
            
            leftAvg, leftSum, leftNum = helper(node.left)
            rightAvg, rightSum, rightNum = helper(node.right)
            
            maxAvg = max(maxAvg, leftAvg, rightAvg)
            
            nodeSum, nodeNum = leftSum + rightSum + node.val, leftNum + rightNum + 1
            
            nodeAvg = (nodeSum)/nodeNum
            
            maxAvg = max(maxAvg, nodeAvg)
            
            return nodeAvg, nodeSum, nodeNum
        
        
        helper(root)
        
        return maxAvg
        