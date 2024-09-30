class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = maxSize * [0]
        self.increments = maxSize * [0]
        self.top = -1
        self.maxSize = maxSize        
        
    def push(self, x: int) -> None:
        if self.top < self.maxSize - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1
        
        if self.top == 0:
            returnVal = self.stack[self.top] + self.increments[self.top]
            self.increments[self.top] = 0
            self.top -= 1
            return returnVal
        
        returnVal = self.stack[self.top] + self.increments[self.top]
        
        self.increments[self.top - 1] += self.increments[self.top]
        self.increments[self.top] = 0
        self.top -= 1
        return returnVal

    def increment(self, k: int, val: int) -> None:
        if k - 1 <= self.top:
            self.increments[k - 1] += val
        else:
            if self.top >= 0:
                self.increments[self.top] += val
                


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)