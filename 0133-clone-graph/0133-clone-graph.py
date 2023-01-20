"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return None
        
        Q = collections.deque({node})
        nodeMap = dict({node: Node(node.val, [])})
        
        while Q:
            tp = Q.pop()
            
            for nxtNode in tp.neighbors:
                if nxtNode not in nodeMap:
                    nodeMap[nxtNode] = Node(nxtNode.val, [])
                    Q.appendleft(nxtNode)
                nodeMap[tp].neighbors.append(nodeMap[nxtNode])
        
        
        return nodeMap[node]
        