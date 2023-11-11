# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import numpy as np

class Solution:
    def getMatches(self, word1, word2) -> int:
        return np.sum(np.array(list(word1)) == np.array(list(word2)))
    
    def getHistogram(self, words: List[str]) -> List[collections.Counter]:
        histogram = [collections.Counter() for _ in range(6)]
        
        for ind, columnWord in enumerate(zip(*words)):
            histogram[ind] = collections.Counter(columnWord)
        
        return histogram
    
    def getWordScore(self, word: str, histogram: List[collections.Counter]) -> int:
        """
        Returns the score of a specific word by adding the histogram scores
        
        """
        
        characterScores = np.array([histogram[ind][char] for ind, char in enumerate(word)])
        
        return np.sum(characterScores)
    
    def getBestWord(self, words: List[str]) -> None:
        """
        Gets the best word in terms of the word score from words
        """
        histogram = self.getHistogram(words)
        
        wordScores = [self.getWordScore(word, histogram) for word in words]
        
        # print("wordScores: ", sorted(list(zip(wordScores, words) ),reverse=True))
        return words[np.argmax(wordScores)]
    
    def pruneWordList(self, words: List[str], bestWord: str, numMatches: int) -> None:
        """
        Prunes the word list to only retain the number of matches we got.
        """
        
        
        return list(filter(lambda word: self.getMatches(word, bestWord) == numMatches, words))
    
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # numGuesses =  10
        
        for numGuess in range(30):
            bestWord = self.getBestWord(words)
            numMatches = master.guess(bestWord)
            
            # print("words: ", words)
            # print("bestWord: ", bestWord)
            # print("numMatches: ", numMatches)
            # print()
            
            if numMatches == 6:
                return
            
            if numMatches == -1:
                continue
            
            words = self.pruneWordList(words, bestWord, numMatches)