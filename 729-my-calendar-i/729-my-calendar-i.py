from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList(key = lambda x: x[0])
        
    
    def __search__(self, start: int, end: int) -> bool:
        for x1, x2 in self.intervals:
            if max(x1, start) <= min(x2, end):
                return True
        return False
        
    def book(self, start: int, end: int) -> bool:
        if self.__search__(start, end - 0.5):
            return False
        
        self.intervals.add([start, end-0.5])
        
        # print("start, end", start, end)
        # print("intervals: ", self.intervals)
        # print()
        return True
        
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)