"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        possibleRoots = set(tree)
        
        for node in tree:
            for child in node.children:
                possibleRoots.remove(child)
        
        return next(iter(possibleRoots))
        