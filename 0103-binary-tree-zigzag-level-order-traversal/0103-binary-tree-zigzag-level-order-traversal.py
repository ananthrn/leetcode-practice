# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        Q = [root]
        
        ans = []
        reverse = False
        while Q:
            
            vals = [node.val for node in Q[::-1]] if reverse else [node.val for node in Q]
            
            ans.append(vals)
            
            nextNodes = []
            
            for node in Q:
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)
            
            Q = nextNodes
                
            reverse = not reverse
        
        return ans
        
        