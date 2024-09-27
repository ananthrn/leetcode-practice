from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlap = 2

    def book(self, start: int, end: int) -> bool:
        
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1
        
        prefixSum = 0
        for count in self.booking_count.values():
            prefixSum += count
            
            if prefixSum > self.max_overlap:
                
                self.booking_count[start] -= 1
                self.booking_count[end] += 1
                
                return False
        
        return True
    

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)