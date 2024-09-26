from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()
        
    
    def __can_add__(self, start: int, end: int) -> bool:
        if not self.intervals:
            return True
        
        if (start, end) in self.intervals:
            return False
        
        prev_index = self.intervals.bisect_left((start, end)) - 1
        next_index = self.intervals.bisect_right((start, end))
        
        if (prev_index == -1 or self.intervals[prev_index][1] <= start) and (next_index == len(self.intervals) or self.intervals[next_index][0] >= end):
            return True
        
        return False
        
    def book(self, start: int, end: int) -> bool:
        if self.__can_add__(start, end):
            self.intervals.add((start, end))
            return True
        
        
        
        # print("start, end", start, end)
        # print("intervals: ", self.intervals)
        # print()
        return False
        
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)