class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutePoints = [
            int(time[0:2]) * 60 + int(time[3:]) for time in timePoints
        ]
        
        minutePoints = sorted(minutePoints)
        
        n = len(timePoints)
        print("minutePoints: ", minutePoints)
        
        diffs = [
            (minutePoints[(index + 1)%n] - minutePoints[index])%1440 for index in range(len(minutePoints))
        ]
        
        print("diffs: ", diffs)
        return min(
diffs        )