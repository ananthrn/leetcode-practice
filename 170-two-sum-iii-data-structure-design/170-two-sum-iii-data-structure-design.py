from sortedcontainers import SortedList
class TwoSum:

    def __init__(self):
        self.l = SortedList([])

    def add(self, number: int) -> None:
        self.l.add(number)

    def find(self, value: int) -> bool:
        start = 0
        end = len(self.l) - 1
        # print("value: ", value)
        # print("self.l", self.l)
        while start < end:
            sm = self.l[start] + self.l[end]
            # print("start, end: ", start, end)
            # print("sm: ", sm)
            
            if sm == value:
                return True
            elif sm > value:
                # print("sm > value")
                end -= 1
            elif sm < value:
                # print("sm < value")
                start += 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)