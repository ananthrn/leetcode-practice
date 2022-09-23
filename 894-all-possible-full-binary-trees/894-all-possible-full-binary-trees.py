# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def helper(n: int) -> List[TreeNode]:
            if n == 0:
                return [None]
            
            if n == 1:
                return [TreeNode(val=0)]
            
            ans = []
            
            for root_index in range(2, n):
                leftNodes = helper(root_index - 1)
                rightNodes = helper(n - root_index)
                
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(
                            val = 0,
                            left = leftNode,
                            right = rightNode,
                        )
                        ans.append(rootNode)
            
            return ans
        
        return helper(n)
                
        