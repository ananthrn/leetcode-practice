class Solution:
    def minSteps(self, s: str, t: str) -> int:
        allCharacs = set(s).union(set(t))
        cCount = collections.Counter(s)
        tCount = collections.Counter(t)

        countDiffs = [cCount[char] - tCount[char] for char in set(s)]

        # print("countDiffs: ", countDiffs)
        totalSwaps = sum([diff for diff in countDiffs if diff > 0])

        return totalSwaps



