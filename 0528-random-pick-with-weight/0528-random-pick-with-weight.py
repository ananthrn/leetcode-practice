import numpy as np
class Solution:

    def __init__(self, w: List[int]):
        np.random.seed(42)
        self.prefWeights = list(w)
        for i in range(1, len(w)):
            self.prefWeights[i] += self.prefWeights[i-1]
        
        
    def pickIndex(self) -> int:
        randomVal = self.prefWeights[-1] * np.random.rand()
        
        
        index = bisect_right(self.prefWeights, randomVal)
        # print("randomVaL: ", randomVal)
        # print("self.prefWeights: ", self.prefWeights)
        # print("index: ", index)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()