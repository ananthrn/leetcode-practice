class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:        
        transpose = [col for col in zip(*matrix)]
        return transpose            