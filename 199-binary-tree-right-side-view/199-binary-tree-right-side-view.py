# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        seen = set()
        Q = collections.deque([(0, root)])
        
        while len(Q) > 0:
            dep, node = Q.pop()
            
            if dep not in seen:
                ans.append(node.val)
                seen.add(dep)
            
            
            for newNode in [node.right, node.left]:
                if newNode is not None:
                    Q.appendleft((dep + 1, newNode))
        
        return ans
        