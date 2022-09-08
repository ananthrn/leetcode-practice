# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        MAX_VAL = 10**4 + 10
        MIN_VAL = -MAX_VAL
        
        ans = 0
        def helper(node: Optional[TreeNode]) -> List[int]:
            '''
            param:
            node: 
            
            returns: A list with values min, max, subtreenodes, isBST
            '''
            nonlocal ans
            if node is None:
                return [MAX_VAL, MIN_VAL, 0, True]
            
            leftMin, leftMax, leftNodes, leftBST = helper(node.left)
            rightMin, rightMax, rightNodes, rightBST = helper(node.right)
            
            
            nodeMin = min(leftMin, rightMin, node.val)
            nodeMax = max(leftMax, rightMax, node.val)
            nodes = leftNodes + rightNodes + 1
            isBST = leftBST and rightBST and (leftMax < node.val < rightMin)
            
            print("node.val: ", node.val)
            print("leftNodes, rightNodes: ", leftNodes, rightNodes)
            print("leftMin, rightMin: ", leftMin, rightMin)
            print("leftMax, rightMax: ", leftMax, rightMax)
            print("leftBST, rightBST:", leftBST, rightBST)
            
            print("nodeMin: ", nodeMin)
            print("nodeMax: ", nodeMax)
            print("nodes: ", nodes)
            print("isBST: ", isBST)
            print()
            if isBST:
                ans = max(ans, nodes)
            
            return [
                nodeMin, 
                nodeMax,
                leftNodes + rightNodes + 1,
                isBST
            ]
        
        helper(root)
        
        return ans
        