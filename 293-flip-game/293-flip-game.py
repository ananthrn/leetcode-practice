class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        flipDict = {
            "++": "--",
        }
        
        ans = [
            currentState[0:j] + flipDict[currentState[j:j+2]] + currentState[j+2:] for j in range(len(currentState)-1) if currentState[j:j+2] in flipDict
        ]
        
        return ans
        