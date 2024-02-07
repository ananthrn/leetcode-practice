class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        
        ans = ""
        
        sortedKeys = sorted(counter.keys(), key=lambda key: counter[key], reverse=True)
        for key in sortedKeys :
            ans += key * counter[key]
            
        
        return ans