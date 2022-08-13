# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from enum import Enum

class State(Enum):
    HAS_CAMERA = 1
    COVERED = 2
    NEEDS_COVER = 3
class Solution:
    
            
            
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cameras = 0
        def helper(rootNode: Optional[TreeNode]) -> int:
            nonlocal cameras
            if not rootNode:
                return State.COVERED
            
            leftState = helper(rootNode.left)
            rightState = helper(rootNode.right)
            
            if leftState == State.NEEDS_COVER or rightState == State.NEEDS_COVER:
                cameras += 1
                return State.HAS_CAMERA
            
            if leftState == State.HAS_CAMERA or rightState == State.HAS_CAMERA:
                return State.COVERED
            
            
            return State.NEEDS_COVER
        
        rootState = helper(root)
        if rootState == State.NEEDS_COVER:
            cameras += 1
        
        return cameras
        