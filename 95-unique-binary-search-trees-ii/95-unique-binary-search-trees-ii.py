# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(val = start)]
        
        ans = []
        
        for value in range(start,  end + 1):
            leftNodes = self.helper(start, value - 1)
            rightNodes = self.helper(value + 1, end)
            
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    ans.append(TreeNode(val = value, left=leftNode, right=rightNode))
        
        return ans
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(val = n)]
        
        ans = self.helper(1, n)
        
        return ans
        
        
        
        
        