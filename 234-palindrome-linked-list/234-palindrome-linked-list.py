# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        prevMap = {}
        
        prev = None
        
        cur = head 
        
        while cur != None:
            prevMap[cur] = prev
            prev = cur
            cur = cur.next
        
        tail = head
        
        while tail.next != None:
            tail = tail.next
        
        cur = head
        
        while cur != tail and tail.next != cur:
            print("cur.val", cur.val)
            print("tail.val", tail.val)
            if cur.val != tail.val:
                return False
            cur = cur.next
            tail = prevMap[tail]
        
        return True
        
        
        