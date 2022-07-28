class Logger:

    def __init__(self):
        self.Q = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while len(self.Q) > 0 and self.Q[0][0] <= timestamp - 10:
            self.Q.popleft()
        
        messages = [msg for time, msg in self.Q]
        
        if message in messages:
            return False
        
        self.Q.append([timestamp, message])
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)