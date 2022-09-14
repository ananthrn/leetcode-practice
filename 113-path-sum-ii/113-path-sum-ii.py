# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        currentPath = []
        # currentSum = 
        def helper(root, targetSum) -> None:
            nonlocal ans, currentPath
            if root is None:
                return
            
            
            if root.left is None and root.right is None:
                currentPath.append(root.val)
                if root.val == targetSum:
                    # print("here: ")
                    # print("root.val: ", root.val)
                    # print("currentPath: ", currentPath)
                    ans.append(list(currentPath))
                    # print("ans: ", ans)
                currentPath.pop()
            else:
                currentPath.append(root.val)
                helper(root.left, targetSum - root.val)
                helper(root.right, targetSum - root.val)
                currentPath.pop()
        
        helper(root, targetSum)
        
        return ans