# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        Q = collections.deque([root,])
        maxValues = [root.val] 
        
        while Q:
            tmp = []
            # mxVal = 0
            for node in Q:
                # if node:
                if node.left:
                    tmp.append(node.left)
                    # if mxVal == None:

                if node.right:
                    tmp.append(node.right)
            
            Q = tmp
            mxVal = max([node.val for node in tmp]) if len(tmp) > 0 else None
            if mxVal is not None:
                maxValues.append(mxVal)
        
        return maxValues