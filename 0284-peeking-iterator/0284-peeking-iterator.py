# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked_value is None:
            if not self.iterator.hasNext():
                raise StopIteration()
            self.peeked_value = self.iterator.next()
        
        print("peek: ", self.peeked_value)
        return self.peeked_value
            
            
            

    def next(self):
        """
        :rtype: int
        """
        if self.peeked_value is not None:
            val = self.peeked_value 
            self.peeked_value = None
            print("next: ", val)
            return val

        if not self.iterator.hasNext():
            raise StopIteration()
        
        val = self.iterator.next()
        print("next: ", val)
        return val
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        print("hasNext: ", (self.peeked_value is not None) or self.iterator.hasNext())
        return (self.peeked_value is not None) or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].