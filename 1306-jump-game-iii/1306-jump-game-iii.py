class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {start}
        Q = collections.deque([start])

        while len(Q) > 0:
            tp = Q.pop()
            print("tp, arr[tp]: ", tp, arr[tp])
            if arr[tp] == 0:
                return True
            for nxt in (tp - arr[tp], tp + arr[tp]):
                if 0 <= nxt < len(arr) and nxt not in seen:
                    seen.add(nxt)
                    Q.appendleft(nxt)
        
        return False
