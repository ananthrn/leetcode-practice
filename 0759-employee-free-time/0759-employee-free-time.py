"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [
            interval for employeeIntervals in schedule for interval in employeeIntervals
        ]
        intervals = sorted(intervals, key=lambda interval: interval.start)
        # print("intervals: ", intervals)
        minVal = intervals[0].start
        maxVal = intervals[0].end
        
        freeTimes = []
        
        for interval in intervals[1:]:
            print("minVal, maxVal: ", minVal, maxVal)
            print("interval: ", interval.start, interval.end)
            
            if interval.start > maxVal:
                freeTimes.append(Interval(maxVal, interval.start ))
                minVal = interval.start
                maxVal = interval.end
            else:
                maxVal = max(maxVal, interval.end)
        
        
        
        nonZeroFreeTimes = filter(lambda interval: interval.end > interval.start, freeTimes)
        
        return nonZeroFreeTimes