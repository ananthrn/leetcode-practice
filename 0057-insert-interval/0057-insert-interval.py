class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        left, right = newInterval
        
        answer = []
        for leftVal, rightVal in intervals:
            if rightVal < left:
                answer.append([leftVal, rightVal])
            elif right < leftVal:
                answer.append([left, right])
                left, right = leftVal, rightVal
            else:
                left = min(left, leftVal)
                right = max(right, rightVal)
        answer.append([left, right])
        return answer