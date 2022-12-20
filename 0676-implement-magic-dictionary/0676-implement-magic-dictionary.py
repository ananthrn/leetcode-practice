class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        return any([self.ifOneAway(searchWord, word) for word in self.dictionary])
    
    def ifOneAway(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        mismatches = [1 for (a, b) in zip(word1, word2) if a != b]
        
        return len(mismatches) == 1


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)