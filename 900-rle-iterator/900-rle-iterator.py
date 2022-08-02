class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.ind = 0

    def next(self, n: int) -> int:
        # ind = 0
        print("n: ", n)
        
        while n > 0 and self.ind < len(self.encoding) - 1:
            print("n, ind: ", n, self.ind)
            if n > self.encoding[self.ind]:
                n -= self.encoding[self.ind]
                self.ind += 2
            elif n < self.encoding[self.ind]:
                self.encoding[self.ind] -= n
                n = 0
            elif n == self.encoding[self.ind]:
                n = 0
                self.encoding[self.ind] = 0
        
        print("ans: ", self.encoding[self.ind + 1] if self.ind < len(self.encoding) - 1 else -1)
        return self.encoding[self.ind + 1] if self.ind < len(self.encoding) - 1 else -1
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)