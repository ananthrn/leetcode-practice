class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordsPossible = list(filter(lambda word: collections.Counter(word) <collections.Counter(chars), words))
        
        return sum([len(word) for word in wordsPossible])
        