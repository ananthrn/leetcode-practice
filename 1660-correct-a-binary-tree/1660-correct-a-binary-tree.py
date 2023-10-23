# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()
        def correctTree(node: TreeNode, parent: TreeNode) -> bool:
            if node is None:
                return False
            
            
            if node.right and node.right.val in seen:
                print(f"{node.val} is the invalid node")
                print("Seen: ", seen)
                print("parent.val: ", parent.val)
                if parent.right and parent.right.val == node.val:
                    parent.right = None
                elif parent.left and parent.left.val == node.val:
                    # print("here: ")
                    parent.left = None
                    
                return True
            
            seen.add(node.val)
            
            checkRight = correctTree(node.right, node)
            if checkRight:
                return True
            
            checkLeft = correctTree(node.left, node)
            if checkLeft:
                return True
            
        
            return False
        
        correctTree(root, None)
        return root
        