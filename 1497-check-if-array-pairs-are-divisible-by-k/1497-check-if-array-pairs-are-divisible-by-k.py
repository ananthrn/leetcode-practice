class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modCounts = collections.Counter(map(lambda val: val % k, arr))
        print("modCounts: ", modCounts)
        
        for key in modCounts:
            print("key: ", key)
            print("k - key: ", k - key)
            print("modCounts[key]: ", modCounts[key])
            print("modCounts[k - key]: ", modCounts[k - key])
            print()
            
        return all(
            modCounts[key] == modCounts[(k - key) % k] if (k - key)%k != key else modCounts[key]%2 == 0 for key in modCounts
        )
    