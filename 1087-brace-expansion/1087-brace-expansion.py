import re

class Solution:
    def expand(self, s: str) -> List[str]:
        s = s.replace("{", "#")
        s = s.replace("}", "#")
        allChars = s.split("#")
        
        allOptions = []
        
        for ind, val in enumerate(allChars):
            print("ind, val: ", ind, val)
            allOptions.append(val.split(","))
        
        print("allOptions: ", allOptions)
        
        if len(allOptions[0]) == 0:
            allOptions = allOptions[1:]
        answers = [""]
        
        for option in allOptions:
            newAnswers = []
            for char in option:
                for answer in answers:
                    newAnswers.append(answer + char)
            
            answers = newAnswers
        
        
        return sorted(answers)
        
        