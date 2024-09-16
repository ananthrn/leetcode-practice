class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        
        prefXors = n * [0]
        
        prefXors[0] = arr[0]
        
        for index in range(1, n):
            prefXors[index] = prefXors[index - 1] ^ arr[index]
            
        
        answers = [
            prefXors[right] ^ prefXors[left - 1] if left > 0 else prefXors[right] for left, right in queries
        ]
        
        return answers