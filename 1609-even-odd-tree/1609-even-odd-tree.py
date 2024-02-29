# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        
        oddParity = 1
        while queue:
            
            vals = [node.val for node in queue]
            
            # check parity 
            if not all([val % 2 == oddParity for val in vals]):
                print("parity error:")
                print(f"vals: {vals}")
                print(f"oddParity: {oddParity}")
                
                return False
            
            orderCheck = lambda a, b: a < b if oddParity == 1 else a > b
            
            # check sortedness
            if not all([orderCheck (vals[i], vals[i+1]) for i in range(len(vals) -1 )]):
                print("sortedness error:")
                print(f"vals: {vals}")
                # print(f"oddParity: {oddParity}")
                return False
            
            nxt = []
            
            for node in queue:
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            
            queue = nxt
            oddParity = 1 - oddParity
        
        return True
        