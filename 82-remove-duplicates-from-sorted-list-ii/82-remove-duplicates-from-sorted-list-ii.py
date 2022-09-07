# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        
        while cur is not None:
            follow = cur.next
            
            while follow is not None and follow.val == cur.val:
                follow = follow.next
            
            if cur.next == follow:
                prev = cur
            else:
                if prev:
                    prev.next = follow
                else:
                    head = follow
            
            cur = follow
        
        return head
        