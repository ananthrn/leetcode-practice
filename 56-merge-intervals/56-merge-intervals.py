class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        minVal = intervals[0][0]
        maxVal = intervals[0][1]
        
        ans = []
        
        for interval in intervals[1:]:
            if interval[0] > maxVal:
                ans.append([minVal, maxVal])
                minVal, maxVal = interval[0], interval[1]
            else:
                maxVal = max(maxVal, interval[1])
        
        ans.append([minVal, maxVal])
        
        return ans
        