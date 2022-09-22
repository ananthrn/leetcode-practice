class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([string[::-1] for string in s.split()])
        