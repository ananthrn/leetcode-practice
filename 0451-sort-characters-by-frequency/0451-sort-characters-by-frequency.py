class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        
        ans = []
        
        sortedKeys = sorted(counter.keys(), key=lambda key: counter[key], reverse=True)
        for key in sortedKeys :
            ans.append(key * counter[key])
            
        
        return "".join(ans)