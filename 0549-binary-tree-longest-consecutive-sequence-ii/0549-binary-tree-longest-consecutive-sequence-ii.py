# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        MAX_LEN = 1
        def helper(rootNode) -> List[int]:
            nonlocal MAX_LEN
            if rootNode is None:
                return [0, 0]
            
            inc, dec = 1, 1
            
            for nextNode in (rootNode.left, rootNode.right):
                if nextNode is not None:
                    incNext, decNext = helper(nextNode)
                    
                    if nextNode.val == rootNode.val + 1:
                        dec = max(dec, decNext + 1)
                    
                    if nextNode.val == rootNode.val - 1:
                        inc = max(inc, incNext + 1)
            
            print("rootNode.val: ", rootNode.val)
            print("inc, dec: ", inc, dec)
            print("bestPath: ", inc + dec - 1)
            print()
            MAX_LEN = max(MAX_LEN, inc + dec - 1)
            return inc, dec
        
        helper(root)
        
        return MAX_LEN
        