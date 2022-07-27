from sortedcontainers import SortedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.orderedMap = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        vl = -1
        
        if key in self.orderedMap:
            vl = self.orderedMap[key]
            self.orderedMap.move_to_end(key)
        
        return vl
            
            

    def put(self, key: int, value: int) -> None:
        if key in self.orderedMap:
            del self.orderedMap[key]
        
        self.orderedMap[key] = value
        
        if len(self.orderedMap) > self.capacity:
            _ = self.orderedMap.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)