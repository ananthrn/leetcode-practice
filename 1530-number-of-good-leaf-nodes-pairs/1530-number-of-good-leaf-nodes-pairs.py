# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        closePairs = dict()
        numPairs = 0
        def helper(root, depth) -> Dict[int, int]:
            nonlocal numPairs, closePairs
            if root is None:
                return collections.Counter()
            
            if root.left is None and root.right is None:
                return collections.Counter([depth])
            
            leftCounter = helper(root.left, depth + 1)
            rightCounter = helper(root.right, depth + 1)
            
            for leftDepth, leftCount in leftCounter.items():
                for rightDepth, rightCount in rightCounter.items():
                    leftDist = leftDepth - depth
                    rightDist = rightDepth - depth
                    
                    if leftDist + rightDist <= distance:
                        # closePairs.add((min(leftVal, rightVal), max(leftVal, rightVal), leftDist + rightDist))
                        # closePairs[(min(leftVal, rightVal), max(leftVal, rightVal))] = leftDist + rightDist
                        numPairs += leftCount * rightCount
                    
            joinedCounter = leftCounter + rightCounter
            
            joinedCounter = Counter({dep: count for (dep, count) in joinedCounter.items() if dep - depth <= distance})
            
                        
            return joinedCounter
            
        helper(root, 0)
        
        print("closePairs: ", closePairs)
        return numPairs
    
        
        
        
        
        