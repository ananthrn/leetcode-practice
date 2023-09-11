class Solution:
    def minOperations(self, n: int) -> int:
        binRep = list(bin(n)[2:][::-1] + "0")
        print("n: ", n)
        print("binRep: ", binRep)
        startInd = 0 
        finalAnswer = 0
        while startInd < len(binRep):
            if binRep[startInd] == '0':
                startInd += 1
            elif binRep[startInd] == '1' and (startInd == len(binRep) - 1 or binRep[startInd + 1] == '0'):
                startInd += 1
            else:
                finalAnswer += 1
                nextInd = startInd
                while nextInd < len(binRep) and binRep[nextInd] == '1':
                    binRep[nextInd] = '0'
                    nextInd += 1
                    
                startInd = nextInd
                if startInd < len(binRep):
                    binRep[startInd] = '1'
                
        
        return finalAnswer + len(list(filter( lambda x: x == '1', binRep)))