class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(1000)]
        self.hash = lambda x: x%1000
        
    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        
        if any(k == key for k, _ in self.map[index]):
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    self.map[index][i] = (key, value)
        else:
            self.map[index].append((key, value))

    def get(self, key: int) -> int:
        index = self.hash(key)
        
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)