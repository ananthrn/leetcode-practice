# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def dfs(node: TreeNode, par: TreeNode):
            nonlocal startNode
            if node is None:
                return
            
            # print("node.val: ", node.val)
            
            if node.val == start:
                startNode = node
                
            parent[node] = par
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        
        def getTime(node: TreeNode, time: int):
            if node is None:
                return
            
            if node.val in seen:
                return
            
            timeInfected[node.val] = time
            seen.add(node.val)
            
            for nextNode in (node.left, node.right, parent[node]):
                getTime(nextNode, time + 1)
                
                
        parent = dict()
        startNode = None
        
        dfs(root, None)
        
        print("startNode: ", startNode.val)
        timeInfected = dict()
        seen = set()
        
        getTime(startNode, 0)
        
        return max(timeInfected.values())
                
            