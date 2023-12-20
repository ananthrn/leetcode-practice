class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest, secondSmallest = sorted(prices)[0:2]
        
        if smallest + secondSmallest <= money:
            return money - smallest - secondSmallest
        else:
            return money
        