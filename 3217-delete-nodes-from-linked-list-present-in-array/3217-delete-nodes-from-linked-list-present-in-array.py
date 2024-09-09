# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def helper(node: Optional[ListNode],) -> Optional[ListNode]:
            if node is None:
                return None
            
            if node.val in numSet:
                return helper(node.next)
            
            else:
                node.next = helper(node.next)
                return node
        
        numSet = set(nums)
        sentinel = ListNode(val=-1, next=head)
        helper(sentinel)
        
        return sentinel.next 
    
            
            
            
        
        
        