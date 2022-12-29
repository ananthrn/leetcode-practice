import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.lock = threading.Lock()
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.lock.acquire()
        
        self.queue.append(element)
        
        self.lock.release()
        self.pulling.release()
        
    def dequeue(self) -> int:
        self.pulling.acquire()
        self.lock.acquire()
        
        val = self.queue.popleft()
        
        self.lock.release()
        self.pushing.release()
        
        return val
    
    def size(self) -> int:
        return len(self.queue)
        