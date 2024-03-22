class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join(filter(lambda char: char not in set("aeiou"), s))
        