
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        def findHelper(arr1, arr2, medianElements):
            start, end = 0, len(arr1) - 1

            while start <= end:
                mid = (start + end)//2
                numElementsArr2Min = bisect.bisect_left(arr2, arr1[mid])
                numElementsArr2Max = bisect.bisect_right(arr2, arr1[mid])

                if mid + numElementsArr2Min <= medianElements <= mid + numElementsArr2Max:
                    return arr1[mid]
                elif mid + numElementsArr2Max < medianElements:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return None
        
        medianElements = (m + n)//2
        if  (m + n)%2 == 1:
            findHelperNums1 = findHelper(nums1, nums2, medianElements)
            findHelperNums2 = findHelper(nums2, nums1, medianElements)
            median =  findHelperNums1 if findHelperNums1 is not None else findHelperNums2

            return median
        else:
            findHelperNums1 = findHelper(nums1, nums2, medianElements)
            findHelperNums2 = findHelper(nums2, nums1, medianElements)

            median1 = findHelperNums1 if findHelperNums1 is not None else findHelperNums2

            findHelperNums1Median2 = findHelper(nums1, nums2, medianElements - 1)
            findHelperNums2Median2 = findHelper(nums2, nums1, medianElements - 1)

            median2 = findHelperNums1Median2 if findHelperNums1Median2 is not None else findHelperNums2Median2
            return (median1 + median2)/2
        


        