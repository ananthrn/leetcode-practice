# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def backtrack(node: 'ImmutableListNode') -> None:
            if node is None:
                return 
            
            backtrack(node.getNext())
            
            node.printValue()
        
        backtrack(head)
        