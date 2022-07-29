from sortedcontainers import SortedDict
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [SortedDict() for i in range(length)]
        for index in range(length):
            self.array[index][0] = 0
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val
        

    def snap(self) -> int:
        val = self.snap_id
        self.snap_id += 1
        return val

    def get(self, index: int, snap_id: int) -> int:
        
        if snap_id in self.array[index]:
            return self.array[index][snap_id]
        
        prev_snap_index = self.array[index].bisect_left(snap_id) - 1
        print("index, snap_id, prev_snap_index: ", index, snap_id, prev_snap_index)
        print("array[index]: ", self.array[index])
        prev_snap_id, prev_value =  self.array[index].peekitem(prev_snap_index)
        print("prev_snap_id, prev_value: ", prev_snap_id, prev_value)
        return prev_value

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)