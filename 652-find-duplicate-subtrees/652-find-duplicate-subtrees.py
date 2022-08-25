# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cache = dict()
        subtrees = defaultdict(list)
        
        def dfs(root):
            if not root:
                return "#"
            leftVal = dfs(root.left)
            rightVal = dfs(root.right)
            
            tot = str(root.val) + " " + leftVal + " " + rightVal
            
            
            if cache.get(tot, 0) == 1:
                subtrees[tot] = root
            
            cache[tot] = cache.get(tot, 0) + 1
            print("tot: ", tot)
            print("occurrences: ", cache.get(tot, 0))
            print()
            return tot
        
        dfs(root)
        
        ans = [val for val in subtrees.values()]
        
        return ans
        
        