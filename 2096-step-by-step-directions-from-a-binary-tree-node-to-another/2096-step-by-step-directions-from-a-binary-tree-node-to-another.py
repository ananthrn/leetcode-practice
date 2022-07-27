# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRootDirections(self, root: Optional[TreeNode], value: int) -> Tuple[bool, str]:
        if(root == None):
            return False, ""
        
        if(root.val == value):
            return True, ""
        
        leftCheck, leftDirs = self.getRootDirections(root.left, value)
        
        if(leftCheck):
            return True, 'L' + leftDirs
        
        rightCheck, rightDirs = self.getRootDirections(root.right, value)
        
        if(rightCheck):
            return True, 'R' + rightDirs
        
        return False, ""
        
        
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        startCheck, startDirs = self.getRootDirections(root, startValue)
        destCheck, destDirs = self.getRootDirections(root, destValue)
        
        assert(startCheck and destCheck)
        
        i = 0
        
        while (i < min(len(startDirs), len(destDirs)) and startDirs[i] == destDirs[i]):
            i+=1
            
        return (len(startDirs) - i) * 'U' + destDirs[i:]
        
        