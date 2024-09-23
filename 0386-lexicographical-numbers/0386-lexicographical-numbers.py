class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def generate_lexicographic(start_number: int) -> None:
            if start_number > n:
                return
            
            result.append(start_number)
            for next_digit in range(10):
                next_number = start_number * 10  + next_digit
                
                if next_number <= n:
                    generate_lexicographic(next_number)
                else:
                    return
        
        
        result = []
        
        for first_digit in range(1, 10):
            generate_lexicographic(first_digit)
        
        
        return result