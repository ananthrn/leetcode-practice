import sortedcontainers
class MRUQueue:

    def __init__(self, n: int):
        self.sd = sortedcontainers.SortedDict(
            {
                key: key for key in range(1, n + 1)
            }
        ) 
        
        self.maxKey = n + 1

    def fetch(self, k: int) -> int:
        _, value = self.sd.popitem(index=k - 1)
        
        self.sd[self.maxKey] = value
        self.maxKey += 1
        
        return value


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)