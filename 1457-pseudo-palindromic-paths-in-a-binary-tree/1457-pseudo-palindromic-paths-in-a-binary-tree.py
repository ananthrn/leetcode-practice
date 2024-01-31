# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isLeaf(node: Optional[TreeNode]) -> bool:
            return node is not None and node.left is None and node.right is None
        
        def isPalindrome(cnt: collections.Counter) -> bool:
            return len([key for key, value in cnt.items() if value%2 == 1]) <= 1
        
        ans = 0
        cnt = collections.Counter()
        
        def helper(node: Optional[TreeNode]):
            nonlocal ans, cnt
            
            if node is None:
                return
            
            if isLeaf(node):
                cnt[node.val] += 1
                if isPalindrome(cnt):
                    ans += 1
                cnt[node.val] -= 1
            else:
                cnt[node.val] += 1
                helper(node.left)
                helper(node.right)
                cnt[node.val] -= 1
        
        helper(root)
        
        return ans
        
        