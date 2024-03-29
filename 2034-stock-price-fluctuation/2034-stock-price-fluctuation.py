from sortedcontainers import SortedList, SortedDict

class StockPrice:

    def __init__(self):
        self.prices = SortedList()
        self.timeToPrice = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.timeToPrice:
            self.prices.add(price)
            self.timeToPrice[timestamp] = price
            return
        
        currentPrice = self.timeToPrice[timestamp]
        self.prices.remove(currentPrice)
        self.prices.add(price)
        self.timeToPrice[timestamp] = price
        
        return

    def current(self) -> int:
        latestTimeStamp, latestPrice = self.timeToPrice.peekitem()
        return latestPrice

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()