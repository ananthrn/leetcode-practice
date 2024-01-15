class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winLossRecord = dict()

        for winner, loser in matches:
            if winner not in winLossRecord:
                winLossRecord[winner] = [0, 0]
            winLossRecord[winner][0] += 1

            if loser not in winLossRecord:
                winLossRecord[loser] = [0, 0]
            winLossRecord[loser][1] += 1
        
        notLost = [player for player, (wins, losses) in winLossRecord.items() if losses == 0]
        lostOnce = [player for player, (wins, losses) in winLossRecord.items() if losses == 1]

        return [sorted(notLost), sorted(lostOnce)]
