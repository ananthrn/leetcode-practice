class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        aliceRemovals = len(list(filter(lambda ind : colors[ind - 1: ind + 2] == "AAA", [ind for ind in range(1, len(colors) - 1)])))
        
        bobRemovals = len(list(filter(lambda ind : colors[ind - 1: ind + 2] == "BBB", [ind for ind in range(1, len(colors) - 1)])))
        print("aliceRemovals, bobRemovals: ", aliceRemovals, bobRemovals)
        return aliceRemovals > bobRemovals
        
        