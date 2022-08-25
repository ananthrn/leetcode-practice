# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        to_delete.add(0)
        
        trees = []
        def dfs(root, parent):
            if not root:
                return
            
            dfs(root.left, root)
            dfs(root.right, root)
            
            if (root.left != None) and root.left.val in to_delete:
                root.left = None
            if (root.right != None) and root.right.val  in to_delete:
                root.right = None
                
            if (
                root.val not in to_delete 
                and (not parent or parent.val in to_delete)
            ):
                trees.append(root)
            
            
        
        dfs(root, None)
        
        return trees
            
                
        