# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def dfs(rootNode, val, length):
            if rootNode is None:
                return 0
            
            length = length + 1 if (rootNode.val == val + 1) else 1

            return max(
                length,
                dfs(rootNode.left, rootNode.val, length),
                dfs(rootNode.right, rootNode.val, length)
            )

        return dfs(root, 1_00_000, 1)
        