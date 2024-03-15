class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append(
                (start, 1)
            )
            
            events.append(
                (end, 0)
            )
        
        events = sorted(events)
        
        numMeetings = 0
        
        maxMeetings = 0
        for time, isStart in events:
            if isStart:
                numMeetings += 1
            else:
                numMeetings -= 1
            
            maxMeetings = max(maxMeetings, numMeetings)
        
        return maxMeetings
            
        