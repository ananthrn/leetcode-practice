class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def shiftString(s, direction, amount) -> s:
            amount = amount % len(s)
            if direction == 1:
                print("")
                return s[len(s)-amount:] + s[:len(s)-amount] 
            else:
                return s[amount:] + s[:amount] 
        
        
        for direction, amount in shift:
            s = shiftString(s, direction, amount)
            print(s)
        
        return s
        