# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getCount(self, root) -> Counter:
        if root is None:
            return Counter()
        
        if root.val == '+':
            return self.getCount(root.left) + self.getCount(root.right)
        else:
            return Counter({root.val: 1})
        
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        return self.getCount(root1) == self.getCount(root2)