class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transforms = set()
        
        for word in words:
            transform = ''.join([morseCode[ord(char) - ord('a')] for char in word])
            transforms.add(transform)
        
        return len(transforms)
        