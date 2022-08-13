"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # possibleRoot = tree[0]
        value_xor = 0
        
        for node in tree:
            value_xor ^= node.val
            for child in node.children:
                value_xor ^= child.val
        
        for node in tree:
            if node.val == value_xor:
                return node
                    