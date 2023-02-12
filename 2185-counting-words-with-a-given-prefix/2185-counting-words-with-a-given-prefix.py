class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(list(filter(lambda word: word[0:len(pref)] == pref, words)))
        