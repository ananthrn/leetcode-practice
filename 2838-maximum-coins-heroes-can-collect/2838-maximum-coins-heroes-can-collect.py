class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n = len(heroes)
        m = len(monsters)
        
        coinMonsterZipped = list(sorted(zip(monsters, coins)))
        coinsPrefixSum = [coin for _, coin in coinMonsterZipped]
        
        for index in range(1, m):
            coinsPrefixSum[index] += coinsPrefixSum[index - 1]
            
        monsters = sorted(monsters)
        
        
        answers = n * [None]
        
        for index, hero in enumerate(heroes):
            monsterIndex = bisect.bisect_right(monsters, hero) - 1
            
            if monsterIndex >= 0:
                answers[index] = coinsPrefixSum[monsterIndex]
            else:
                answers[index] = 0
        
        return answers