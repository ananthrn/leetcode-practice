class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sumOfAP(numElements: int, startingElement: int, endingElement: int) -> int:
            return (numElements * (startingElement + endingElement))//2
        
        def check(val: int) -> bool:
            """
            returns true if nums[index] == val gives a valid answer
            """
            #calculate leftSum
            
            leftSum = 0
            elementsLeft = index + 1
            
            if elementsLeft >= val:
                leftSum = (elementsLeft - val) + sumOfAP(val, val, 1)
            else:
                leftSum = sumOfAP(elementsLeft, val, val - (elementsLeft - 1))
                
            #calculate rightSum
            
            rightSum = 0
            elementsRight = (n - 1) - (index + 1) + 1
            
            if elementsRight >= (val - 1):
                rightSum = (elementsRight - (val - 1)) + sumOfAP(val - 1, val - 1, 1)
            else:
                rightSum = sumOfAP(elementsRight, val - 1, val - 1 - (elementsRight - 1))
            
            # print("n, index, maxSum: ", n, index, maxSum)
            # print("val: ", val)
            # print("leftSum: ", leftSum)
            # print("rightSum: ", rightSum)
            # print("totalSum: ", leftSum + rightSum)
            # print("check?: ", leftSum + rightSum <= maxSum)
            # print()
            
            return leftSum + rightSum <= maxSum
        
        start, end = 1, maxSum 
        maxNumsIndex = -1
        
        while start <= end:
            mid = (start + end)//2
            chk = check(mid)
            if chk:
                maxNumsIndex = max(maxNumsIndex, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return maxNumsIndex
                
        