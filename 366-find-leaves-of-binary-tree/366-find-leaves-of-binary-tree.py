# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(src: Optional[TreeNode]) -> int:
            if(src is None):
                return -1
            
            leftHeight = dfs(src.left)
            rightHeight = dfs(src.right)
            
            height = max(leftHeight, rightHeight) + 1
            
            if(len(ans) -1 < height):
                ans.append([])
                
            ans[height].append(src.val)
            
            return height
        
        dfs(root)
        
        return ans
            
            
        