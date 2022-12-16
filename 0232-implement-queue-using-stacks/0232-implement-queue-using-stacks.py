class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            x = self.stack1.pop()
            self.stack2.append(x)
        
        returnVal = self.stack2.pop()
        
        while self.stack2:
            x = self.stack2.pop()
            self.stack1.append(x)
        
        return returnVal

    def peek(self) -> int:
        while self.stack1:
            x = self.stack1.pop()
            self.stack2.append(x)
        
        returnVal = self.stack2[-1]
        
        while self.stack2:
            x = self.stack2.pop()
            self.stack1.append(x)
        
        return returnVal


    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()