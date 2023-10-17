# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        opMap = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y,
            4: lambda x, y: x != y,
            5: lambda x: not x
        }
        
        @cache
        def minFlipsHelper(node: Optional[TreeNode], result: bool) -> int:
            # print("node.val", node.val)
            if node.left is not None and node.right is not None:
                minFlips = 1000000
                
                for leftVal in [True, False]:
                    for rightVal in [True, False]:
                        if opMap[node.val](leftVal, rightVal) == result:
                            minFlips = min(minFlips, minFlipsHelper(node.left, leftVal) + minFlipsHelper(node.right, rightVal))
                return minFlips
                
            
            elif node.left is not None:
                assert node.val == 5, "not a not node"
                
                return minFlipsHelper(node.left, not result)
            elif node.right is not None:
                assert node.val == 5, "not a not node"
                return minFlipsHelper(node.right, not result)
            else:
                return 1 if node.val != result else 0
        
        return minFlipsHelper(root, result)
            
                
            
            