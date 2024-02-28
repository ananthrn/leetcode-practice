# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        depthToVals = collections.deque()
        
        Q = collections.deque()
        
        Q.append(root)
        
        currentDepth = 0
        
        while Q:
            depthToVals.appendleft([node.val for node in Q])
            
            nxtLevel =  []
            
            for elem in Q:
                if elem.left is not None:
                    nxtLevel.append(elem.left)
                
                if elem.right is not None:
                    nxtLevel.append(elem.right)
            
            currentDepth += 1
            
            Q = nxtLevel
        
        return depthToVals
        
        
            
            