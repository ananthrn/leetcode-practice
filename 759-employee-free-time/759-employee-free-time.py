"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class SortedIntervals:
    def __init__(self):
        self.intervals = []
    
    def insert(self, newInterval):
        newIntervals = []
        
        minVal = newInterval.start
        maxVal = newInterval.end
        
        for interval in self.intervals:
            if interval.end < minVal:
                # In this case the interval is completely to the left
                # so we can just append it without any concerns
                newIntervals.append(interval)
            else:
                if maxVal >= interval.start:
                    # In this case part of our extended union interval we need to pus
                    # overlaps with the next one, so we add it to the union
                    # by updating the max value
                    minVal = min(minVal, interval.start)
                    maxVal = max(maxVal, interval.end)
                else:
                    newIntervals.append(Interval(minVal, maxVal))
                    minVal, maxVal = interval.start, interval.end
        
        newIntervals.append(Interval(minVal, maxVal))
        self.intervals = newIntervals
                    
    def getFreeTime(self):
        freeTime = []
        
        for i in range(len(self.intervals) - 1 ):
            freeTime.append(Interval(self.intervals[i].end, self.intervals[i+1].start))
            
        return freeTime
    
    def print(self):
        for i, interval in enumerate(self.intervals):
            print(f"interval {i}: ", interval.start, interval.end)
        print()
    
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        SI = SortedIntervals()
        
        for employee in schedule:
            for interval in employee:
                SI.insert(interval)
        SI.print()
        return SI.getFreeTime()