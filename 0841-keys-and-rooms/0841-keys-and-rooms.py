class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfs(src: int) -> bool:
            Q = collections.deque([src])
            seen = set()
            
            while Q:
                tp = Q.pop()
                
                if tp not in seen:
                    seen.add(tp)
                    if len(seen) == len(rooms):
                        return True
                    
                    for nxt in rooms[tp]:
                        if nxt not in seen:
                            Q.appendleft(nxt)
            
            print("seen: ", seen)
            return len(seen) == len(rooms)
        
        return bfs(0)
                    
        