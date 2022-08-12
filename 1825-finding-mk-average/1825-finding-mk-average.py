from sortedcontainers import SortedList
import numpy as np
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.numbers = []
        self.numSorted = SortedList()
        self.total = self.k_small = self.k_large = 0
    
    def addNum(self, num: int) -> None:
        self.total += num
        # Find index of the value in log(m) time using sortedList
        index = self.numSorted.bisect_left(num)
        
        # if num is in bottom k add to self.k_small
        if index < self.k:
            self.k_small += num
            # remove from k_small the element that gets promoted
            if len(self.numSorted) >= self.k:
                self.k_small -= self.numSorted[self.k - 1]
        # if num is in largest k add to self.k_large
        if index >= len(self.numSorted) - self.k + 1:
            self.k_large += num
            # remove from k_alrge the element that gets promoted
            if len(self.numSorted) >= self.k:
                self.k_large -= self.numSorted[-self.k]
        # add it to the sortedList finally
        self.numSorted.add(num)
    
    def removeNum(self, num: int) -> None:
        self.total -= num
        # Find index of the value in log(m) time using sortedList
        index = self.numSorted.bisect_left(num)
        
        # if num is in bottom k remove from self.k_small
        if index < self.k:
            self.k_small -= num
            # add to k_small the element that gets demoted
            if len(self.numSorted) > self.k:
                self.k_small += self.numSorted[self.k]
        # if num is in largest k subtract from self.k_large
        if index >= len(self.numSorted) - self.k:
            self.k_large -= num
            # remove from k_alrge the element that gets promoted
            if len(self.numSorted) > self.k:
                self.k_large += self.numSorted[-self.k - 1]
        # remove from to the sortedList finally
        self.numSorted.remove(num)
        
    def addElement(self, num: int) -> None:
        self.numbers.append(num)
        
        self.addNum(num)
        
        if len(self.numbers) > self.m:
            valToRemove = self.numbers[-(self.m + 1)]
            self.removeNum(valToRemove)

    def calculateMKAverage(self) -> int:
        if len(self.numbers) < self.m:
            return -1
        
        return (self.total - self.k_small - self.k_large)//(self.m - 2*self.k)
    
        return np.sum(self.numSorted[self.k:-self.k])//(self.m - 2 *self.k)
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()