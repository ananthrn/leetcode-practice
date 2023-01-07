class Solution:
    def confusingNumber(self, n: int) -> bool:
        def getNewNumber(n: int) -> str:
            s = str(n)
            
            if any([badNum in s for badNum in ['2','3', '4', '5','7']]):
                return None
            
            flipped = {
                '0': '0',
                '1': '1',
                '8': '8',
                '6': '9',
                '9': '6',
            }
            
            newS = list(map(lambda x: flipped.get(x), s))
            
            newInt = int("".join(reversed(newS)))
            return newInt
        
        newNumber = getNewNumber(n)
        print("newNumber: ", newNumber)
        return newNumber is not None and newNumber != n
            
        