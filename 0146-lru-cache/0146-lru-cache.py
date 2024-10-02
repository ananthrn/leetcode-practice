from sortedcontainers import SortedList

class ListNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class List:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode(key=None, val=None, next=None, prev=self.head)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        
        self.length = 0
    
    def append(self, key: int, val: int) -> ListNode:
        oldPrev = self.tail.prev 
        
        newListNode = ListNode(key=key, val=val, next=self.tail, prev=oldPrev)
        
        oldPrev.next = newListNode 
        self.tail.prev = newListNode
        
        self.length += 1
        
        # print("self.tail.prev: ", self.tail.prev.key, self.tail.prev.val)
        return self.tail.prev
    
    def appendLeft(self, key: int, val: int) -> ListNode:
        oldNext = self.head.next 
        
        newListNode = ListNode(key=key, val=val, next=oldNext, prev=self.head)
        
        self.head.next = newListNode
        oldNext.prev = newListNode 
        
        self.length +=1
        
        return self.head.next
    
    def pop(self) -> Tuple[int]:
        if self.length == 0:
            return -1, -1
        
        oldPrev = self.tail.prev 
        oldPrevPrev = self.tail.prev.prev 
        
        oldPrevPrev.next = self.tail 
        self.tail.prev = oldPrevPrev 
        
        self.length -= 1
        
        return oldPrev.key, oldPrev.val 
    
    def popLeft(self) -> Tuple[int]:
        if self.length == 0:
            return -1, -1 
        
        oldNext = self.head.next 
        oldNextNext = self.head.next.next
        
        oldPrevPrev.prev = self.head 
        self.head.next = oldNextNext 
        
        self.length -= 1
        
        return oldNext.key, oldNext.val
    
    def deleteNode(self, node: ListNode) -> Tuple[int]:
        if self.length == 0:
            return -1, -1
        
        assert node != self.head and node != self.tail 
        
        oldPrev = node.prev 
        oldNext = node.next 
        
        oldPrev.next = oldNext 
        oldNext.prev = oldPrev 
        
        self.length -= 1
        
        return node.key, node.val 
    
    def getList(self) -> Dict[int, Dict[str, int]]:
        
        self.index = 0
        
        dictionary = {
            
        }
        currentNode = self.head.next
        
        while currentNode != self.tail:
            
            dictionary[self.index] = {
                "key": currentNode.key,
                "val:": currentNode.val
            }
            
            self.index += 1
            currentNode = currentNode.next 
        
        return dictionary
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.list = List()
        
    def get(self, key: int) -> int:
        # print(f"Before Get {key}")
        # print("Current Linked List")
        # print(self.list.getList())
        # print()
        if key in self.dict:
            
            currentNode = self.dict[key]
            print("Deleting: ", currentNode.key, currentNode.val)
            
            currentKey, currentValue = self.list.deleteNode(self.dict[key])
            
            self.dict[key] = self.list.appendLeft(key = currentKey, val = currentValue)
            
            # print(f"After Get {key}")
            # print("Current Linked List")
            # print(self.list.getList())
            # print()
            return currentValue
        
        return -1

    def put(self, key: int, value: int) -> None:
        # print(f"Before: Put {key}: {value}")
        # print("Current Linked List")
        # print(self.list.getList())
        # print()
        
        if key in self.dict:
            oldKey, oldValue = self.list.deleteNode(self.dict[key])
            del self.dict[key]
            # print(f"removed {oldKey}: {oldValue}")
        
        newNode = self.list.appendLeft(key=key, val=value)
        # print("newNode: ", newNode.key, newNode.val)
        self.dict[key] = newNode
        
        if self.list.length > self.capacity:
            keyPopped, valuePopped = self.list.pop()
            # print(f"removed {keyPopped}: {valuePopped}")
            # print("dict: ", self.dict)
            del self.dict[keyPopped]
            
        
        # print(f"After: Put {key}: {value}")
        # print("Current Linked List")
        # print(self.list.getList())
        # print()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)