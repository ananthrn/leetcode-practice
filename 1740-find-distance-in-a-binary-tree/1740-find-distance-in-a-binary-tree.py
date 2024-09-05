# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def constructGraph(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            if parent is not None:
                adj[node.val].add(parent.val)
                adj[parent.val].add(node.val)
            
            constructGraph(node.left, node)
            constructGraph(node.right, node)
        
        def bfs(src: int, dest: int) -> int:
            Q = collections.deque([(0, src)])
            visited = set()
            
            while Q:
                topDistance, topNode = Q.pop()
                
                if topNode == dest:
                    return topDistance
                
                if topNode not in visited:
                    visited.add(topNode)
                    
                    for nextNode in adj[topNode]:
                        if nextNode not in visited:
                            Q.appendleft((topDistance + 1, nextNode))
            
            return -1
        
        adj = collections.defaultdict(set)
        constructGraph(root, None)
        
        return bfs(p, q)
        
        