class Logger:

    def __init__(self):
        self.Q = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print("timestamp, message: ", timestamp, message)
        print("Q: ", self.Q)
        while len(self.Q) > 0 and self.Q[0][0] <= timestamp - 10:
            print(self.Q[0])
            self.Q.popleft()
        
        messages = [msg for time, msg in self.Q]
        
        print("messages: ", messages)
        print()
        if message in messages:
            return False
        
        self.Q.append([timestamp, message])
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)