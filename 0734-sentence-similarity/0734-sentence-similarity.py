class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        pairs = set()
        for word1, word2 in similarPairs:
            pairs.add((word1, word2))
            pairs.add((word2, word1))
        
        return all(
            (word1 == word2 or (word1, word2) in pairs) for (word1, word2) in zip(sentence1, sentence2)
        )
        
        
        
        