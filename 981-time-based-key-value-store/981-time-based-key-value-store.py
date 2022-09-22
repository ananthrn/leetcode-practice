
from sortedcontainers import SortedList
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(lambda: SortedList(key = lambda x: x[0]))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        index = self.map[key].bisect_left((timestamp + 1, "a")) - 1
        if index >= 0 and index < len(self.map[key]):

            return self.map[key][index][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)