from collections import defaultdict
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # return True
        adj = defaultdict(list)
        
        for seq in sequences:
            for j in range(0, len(seq) - 1):
                adj[seq[j]].append(seq[j+1])
        
        print("adj, ", adj)
        cache = {}
        seen = (len(nums) + 1) * [0]
        def dfs(src: int) -> int:
            if src in cache:
                return cache[src]
            
            seen[src] = 1
            currentVal = 0
            
            print("src: ", src)
            print("Adj[src]: ", src)
            for nxt in adj[src]:
                if seen[nxt] == 0:
                    nxtVal = dfs(nxt)
                    if nxtVal == 100:
                        return 100
                    currentVal = min(currentVal, nxtVal)
                elif seen[nxt] == 2:
                    nxtVal = cache[nxt]
                    currentVal = min(currentVal, nxtVal)
                elif seen[nxt] == 1:
                    print("cycle detected")
                    return 100
                else:
                    assert False, "weird loop"
            
            seen[src] = 2
            
            cache[src] = currentVal - 1
            return cache[src]
        
        
        for num in nums:
            if seen[num] == 0:
                val = dfs(num)
                if val == 100:
                    return False
        print("cache: ", cache)
        valueFreq = defaultdict(int)
        for num in nums:
            if num not in cache:
                return False
            else:
                valueFreq[cache[num]] += 1
        
        if any([freq > 1 for freq in valueFreq.values()]):
            return False
        else:
            return True