class MagicDictionary:

    def __init__(self):
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.count = collections.Counter(
            nei for word in self.words for nei in self._genneigbhors(word)
        )

    def search(self, searchWord: str) -> bool:
        nebs = self._genneigbhors(searchWord)
        
        return any(
            [
                self.count[neb] > 1 or self.count[neb] == 1 and searchWord not in self.words for neb in nebs
            ]
        )
    def _genneigbhors(self, word: str) -> List[str]:
        return [
            word[:i] + "*" + word[i+1:] for i in range(len(word))
        ]

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)