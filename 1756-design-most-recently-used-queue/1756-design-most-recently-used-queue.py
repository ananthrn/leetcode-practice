from sortedcontainers import SortedList
class MRUQueue:

    def __init__(self, n: int):
        self.lst = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        val = self.lst[k - 1]
        del self.lst[k-1]
        self.lst.append(val)
        return val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)