# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        def mapHelper(rootNode):
            if rootNode is None:
                return
            
            nodeToNodeCopy[rootNode] = NodeCopy(val=rootNode.val)
            
            mapHelper(rootNode.left)
            mapHelper(rootNode.right)
        
        def leftRightRandomHelper(rootNode):
            if rootNode is None:
                return 
            
            nodeToNodeCopy[rootNode].left = nodeToNodeCopy.get(rootNode.left)
            nodeToNodeCopy[rootNode].right = nodeToNodeCopy.get(rootNode.right)
            nodeToNodeCopy[rootNode].random = nodeToNodeCopy.get(rootNode.random)
            
            leftRightRandomHelper(rootNode.left)
            leftRightRandomHelper(rootNode.right)
        
        nodeToNodeCopy = dict()
        
        
        mapHelper(root)
        
        leftRightRandomHelper(root)
        
        return nodeToNodeCopy.get(root)