class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        """
        
        intervals = sorted(intervals, key=lambda interval: interval[0])
        minVal = intervals[0][0]
        maxVal = intervals[0][1]
        
        ans = []
        for left, right in intervals[1:]:
            if maxVal < left:
                ans.append((minVal, maxVal))
                minVal = left
                maxVal = right
            else:
                maxVal = max(maxVal, right)
        
        ans.append((minVal, maxVal))
        
        return ans