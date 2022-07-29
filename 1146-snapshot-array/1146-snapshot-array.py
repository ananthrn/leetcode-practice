from sortedcontainers import SortedDict
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [SortedDict([(0, 0)]) for i in range(length)]
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        # set the latest snap id;s val
        self.array[index][self.snap_id] = val
        

    def snap(self) -> int:
        # return the previous snap id
        val = self.snap_id
        self.snap_id += 1
        return val

    def get(self, index: int, snap_id: int) -> int:
        # if exists 
        if snap_id in self.array[index]:
            return self.array[index][snap_id]
        # else find the index of the previous snap id (since no updates were made to the index at this exact snap)
        prev_snap_index = self.array[index].bisect_left(snap_id) - 1
        prev_snap_id, prev_value =  self.array[index].peekitem(prev_snap_index)
        return prev_value

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)