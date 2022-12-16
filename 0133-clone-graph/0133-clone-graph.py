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
        nodeMap = dict()

        Q = collections.deque([node])
        seen = set()

        while len(Q) > 0:
            topNode = Q.pop()
            print("topNode.val: ", topNode.val)
            if topNode.val not in seen:
                seen.add(topNode.val)
                nodeMap[topNode.val] = Node(topNode.val, [])

                for neighbor in topNode.neighbors:
                    if neighbor.val not in seen:
                        Q.appendleft(neighbor)
        
        seen = set()
        Q = collections.deque([node])
        
        while len(Q) > 0:
            topNode = Q.pop()
            print("topNode.val: ", topNode.val)
            
            if topNode.val not in seen:
                seen.add(topNode.val)
                nodeMap[topNode.val].neighbors = [nodeMap[neb.val] for neb in topNode.neighbors]
                
                for neighbor in topNode.neighbors:
                    if neighbor.val not in seen:
                        Q.appendleft(neighbor)
        
        
        
        # def helper(srcNode: 'Node') -> None:
        #     nodeMap[]
        return nodeMap[node.val] 