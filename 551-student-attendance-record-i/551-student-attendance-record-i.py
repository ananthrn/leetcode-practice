class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = len([char for char in s if char == 'A'])
        consecLate = s.find("LLL")
        
        return absences < 2 and consecLate == -1