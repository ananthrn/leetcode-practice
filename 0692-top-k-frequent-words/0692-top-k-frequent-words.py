class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        def compare(word1, word2):
            if cnt[word1] != cnt[word2]:
                return cnt[word2] - cnt[word1]
            else:
                if word1 < word2:
                    return -1
                elif word2 > word1:
                    return 1
                else:
                    return 0
                
        cnt = Counter(words)
        
        sortedWords = sorted(cnt.keys(), key=functools.cmp_to_key(compare))
        
        return sortedWords[:k]