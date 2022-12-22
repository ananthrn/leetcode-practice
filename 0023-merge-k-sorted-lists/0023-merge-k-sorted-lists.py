# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        ans = []
        
        
        sl = SortedList(key = lambda x: x.val)
        
        
        for l in lists:
            if l is not None:
                sl.add(l)
        
        ans = []
        
        while len(sl) > 0:
            topNode = sl.pop(0)
            print("topNode.val: ", topNode.val)
            ans.append(topNode)
            if topNode.next is not None:
                sl.add(topNode.next)
                
        if len(ans) == 0:
            return None
        
        for ind, node in enumerate(ans[:-1]):
            node.next = ans[ind+1]
        
        
        ans[-1].next = None
        
        return ans[0]