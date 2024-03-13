class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDict = {
            char: index for index, char in enumerate(order)
        }
        
        sortedList = list(sorted(s, key = lambda char: orderDict.get(char, len(s))))
        
        return "".join(sortedList)