class Solution:
    def minLength(self, s: str) -> int:
        charList = list(s)
        
        while True:
            newList = []
            index = 0
            
            while index < len(charList) - 1:
                if (charList[index], charList[index + 1]) == ("A", "B") or  (charList[index], charList[index + 1]) == ("C", "D"):
                    index += 2
                else:
                    newList.append(charList[index])
                    index += 1
            
            if index == len(charList) - 1:
                newList.append(charList[index])
                
            # print("charList", charList)
            # print("newList: ", newList)
            # print()
            if len(newList) == len(charList):
                return len(newList)
            else:
                charList = newList
        
        
        return 0
            
            