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
            rootIndex = inorder.index(rootVal)
            
            # print("rootIndex: ", rootIndex)
            # print()
            #construct left and right in orders
#             inorderLeft = inorder[0:rootIndex]
#             inorderRight = inorder[rootIndex + 1:]

#             postLeftIndex = max([postorder.index(val) for val in inorderLeft]) if len(inorderLeft) > 0 else -1
#             postLeftIndex = max([postorder.index(val) for val in inorderLeft]) if len(inorderLeft) > 0 else -1 
#             postorderLeft = postorder[0: postLeftIndex + 1]
#             postorderRight = postorder[postLeftIndex + 1: -1]
#             # postorderLeft = [val for val in postorder if val in inorderLeft]
#             # postorderRight = [val for val in postorder if val in inorderRight]
            
            rootNode.right = helper(rootIndex + 1, inorder_right)
            rootNode.left = helper(inorder_left, rootIndex - 1)
            

            return rootNode
        
        return helper(0, len(inorder) - 1)
        
        