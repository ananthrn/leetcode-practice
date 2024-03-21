# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            
            # save the temp next 
            temp_next = curr.next
            
            # make new connections
            curr.next = prev 
            
            # update vars
            prev = curr
            curr = temp_next
        
        return prev
        