# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        def helper(inorder_left: int, inorder_right: int) -> Optional[TreeNode]:
            if inorder_right < inorder_left:
                return None
            
            
            # print("postorder: ", postorder)
            # print("inorder: ", inorder)
            # print("inorder_left, inorder_right: ", inorder_left, inorder_right)
            rootVal = postorder.pop()
            # print("rootVal: ", rootVal)
            
            # print ()
            rootNode = TreeNode(val=rootVal)

            # print("rootVal: ")
            rootIndex = idx_map[rootVal]
            
            # print("rootIndex: ", rootIndex)
            # print()
            
            
            rootNode.right = helper(rootIndex + 1, inorder_right)
            rootNode.left = helper(inorder_left, rootIndex - 1)
            

            return rootNode
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
        
        