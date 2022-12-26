class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        START = 1
        END = 0

        events = []

        for interval in intervals:
            events.append((interval[0], START))
            events.append((interval[1], END))
        
        events = sorted(events) 
        
        maxActiveMeetings = 0
        activeMeetings = 0

        for eventTime, eventType in events:
            if eventType == START:
                activeMeetings += 1
            else:
                activeMeetings -= 1
            
            maxActiveMeetings = max(maxActiveMeetings, activeMeetings)
        
        return maxActiveMeetings


