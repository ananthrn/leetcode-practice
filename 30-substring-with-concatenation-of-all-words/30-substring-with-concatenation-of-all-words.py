class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordMap = dict()
        wordLen = len(words[0])
        allWordsLen = len(words) * (len(words[0]))
        print("allWordsLen", allWordsLen)
        
        for word in words:
            wordMap[word] = wordMap.get(word, 0) + 1
        
        print(wordMap)
        
        def checkString(s: str, wordMap: Dict[str, int]) -> bool:
            # print("s: ", s)
            wordMapCopy = dict(wordMap)
            
            
            
            for i in range(0, len(s), wordLen):
                
                currentString = s[i: i + wordLen]
                if wordMapCopy.get(currentString, 0) > 0:
                    wordMapCopy[currentString] -= 1
                    if wordMapCopy[currentString] == 0:
                        del wordMapCopy[currentString]
                else:
                    return False
            
            return len(wordMapCopy) == 0
        
        
        
        ans = [i for i in range(len(s)) if checkString(s[i: i + allWordsLen], wordMap)]
        
        return ans
        
        
        