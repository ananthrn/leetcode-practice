
from sortedcontainers import SortedList
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        index = self.map[key].bisect_left((timestamp + 1, "ZZZZZZZZZZZZZZZZZZZZZ")) - 1
        # print("self.map[key]: ", self.map[key])
        # print("timestamp: ", timestamp)
        # print("index: ", index)
        if index >= 0 and index < len(self.map[key]):
            # print("ans: ", self.map[key][index][1])
            # print()
            return self.map[key][index][1]
        else:
            # print("ans: ", "")
            # print()
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)