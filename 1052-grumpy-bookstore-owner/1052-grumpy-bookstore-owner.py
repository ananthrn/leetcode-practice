class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        disCustomers = n * [0]
        
        disCustomers[0] = customers[0] if grumpy[0] == 1 else 0
        
        for i in range(1, n):
            disCustomers[i] = disCustomers[i - 1]
            disCustomers[i] += customers[i] if grumpy[i] == 1 else 0
        
        bestVal = disCustomers[minutes - 1]
        
        for j in range(minutes, n):
            bestVal = max(bestVal, disCustomers[j] - disCustomers[j - minutes])
        
        print("customers:", customers)
        print("disCustomers: ", disCustomers)
        print("bestVal: ", bestVal)
        
        return sum(customers) - disCustomers[-1] + bestVal
        