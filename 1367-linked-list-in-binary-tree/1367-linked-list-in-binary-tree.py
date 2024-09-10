# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def DFS(listNode: Optional[ListNode], treeNode: Optional[TreeNode]) -> bool:
            if listNode is None:
                return True
            
            if treeNode is None:
                return False
            
            if listNode.val != treeNode.val:
                return False
            
            return DFS(listNode.next, treeNode.left) or DFS(listNode.next, treeNode.right)
        
        def checkPath(listNode: Optional[ListNode], treeNode: Optional[TreeNode]) -> bool:
            if treeNode is None:
                return False
            
            if DFS(listNode, treeNode):
                return True
            
            return checkPath(listNode, treeNode.left) or checkPath(listNode, treeNode.right)
        
        answer = checkPath(head, root)
        
        return answer
        
        return answer