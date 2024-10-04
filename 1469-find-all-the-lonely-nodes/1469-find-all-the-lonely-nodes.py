# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            if node.left is not None and node.right is None:
                answer.append(node.left.val)
                
            if node.right is not None and node.left is None:
                answer.append(node.right.val)
            
            helper(node.left)
            helper(node.right)
            
        answer = []
        
        helper(root)
        
        return answer
        