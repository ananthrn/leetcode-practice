class Solution:
    def compress(self, chars: List[str]) -> int:
        readIndex = 0
        writeIndex = 0
        
        while readIndex < len(chars):
            if readIndex == len(chars) - 1 or chars[readIndex] != chars[readIndex + 1]:
                
                chars[writeIndex] = chars[readIndex]
                readIndex += 1
                writeIndex += 1
            else:
                nextIndex = readIndex
                while nextIndex < len(chars) and chars[nextIndex] == chars[readIndex]:
                    nextIndex += 1
                reps = nextIndex - readIndex
                
                chars[writeIndex] = chars[readIndex]
                writeIndex += 1
                chars[writeIndex: writeIndex + len(str(reps))] = str(reps)
                
                readIndex = nextIndex
                writeIndex += len(str(reps))
                
                
                
        return writeIndex