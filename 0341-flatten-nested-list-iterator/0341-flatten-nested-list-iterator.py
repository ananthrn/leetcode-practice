# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.listStack = [nestedList]
        self.indexStack = [0]
        
    def next(self) -> int:
        output = self.listStack[-1][self.indexStack[-1]].getInteger()
        self.indexStack[-1] +=1
        return output
    
    def hasNext(self) -> bool:
        while self.listStack and self.indexStack:
            if self.indexStack[-1] < len(self.listStack[-1]):
                if self.listStack[-1][self.indexStack[-1]].isInteger():
                    return True
                else:
                    newList, newIndex = self.listStack[-1][self.indexStack[-1]].getList(), 0
                    self.indexStack[-1] += 1
                    
                    self.indexStack.append(newIndex)
                    self.listStack.append(newList)
            else:
                self.indexStack.pop()
                self.listStack.pop()
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())