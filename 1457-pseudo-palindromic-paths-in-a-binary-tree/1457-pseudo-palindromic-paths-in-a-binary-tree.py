# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        def isPseudoPalindrome(cnt: Dict) -> bool:
            return len([key for key, val in cnt.items() if val%2==1]) <= 1
            
        cnt = Counter()
        ans  = 0
        
        def helper(root):
            nonlocal ans, cnt
            if root is None:
                return 
            
            
            if isLeaf(root):
                cnt[root.val] += 1
                if isPseudoPalindrome(cnt):
                    ans += 1
                cnt[root.val] -= 1
            else:
                cnt[root.val] += 1
                helper(root.left)
                helper(root.right)
                cnt[root.val] -= 1
        
        helper(root)
        return ans
                
                
                
            
            
            
            
        