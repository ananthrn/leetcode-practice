class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.wordSet = set(dictionary)
        self.abbCount = collections.Counter()
        
        for word in self.wordSet:
            self.abbCount[self.getAbbreviation(word)] += 1
            
    def isUnique(self, word: str) -> bool:
        abb = self.getAbbreviation(word)
        
        return self.abbCount[abb] == 0 or (self.abbCount[abb] == 1 and word in self.wordSet)
    
    def getAbbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)