class Pair:
    def __init__(self, word: str, freq: int):
        self.freq = freq
        self.word = word
    
    def __lt__(self, p):
        return self.freq < p. freq or (self.freq == p.freq) and (self.word > p.word)
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
           
        cnt = Counter(words)
        
        minHeap = []
        for word, freq in cnt.items():
            heapq.heappush(minHeap, Pair(word, freq))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        ans = [heapq.heappop(minHeap).word for _ in range(len(minHeap))]
        
        return ans[::-1]