class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
           
        cnt = Counter(words)
        
        sortedWords = sorted(cnt.keys(), key=lambda word: (-cnt[word], word))
        
        return sortedWords[:k]