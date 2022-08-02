class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.empty())
            return -1;
        
        int currentPos = -1;
        int leftIndex = 0;
        int rightIndex = (int)nums.size() - 1;
        
        while(leftIndex <= rightIndex){

            int midIndex = (leftIndex + rightIndex)/2;
            
            if(nums[midIndex] == target)
                return midIndex;
            
            if(nums[leftIndex] <= nums[midIndex]){
                // nums[leftIndex...midIndex] is sorted
                
                if(nums[leftIndex] <= target and target <= nums[midIndex]){
                    rightIndex = midIndex - 1;
                } else {
                    leftIndex = midIndex + 1;
                }
            } else {
                // nums[midIndex...rightIndex] is sorted
                if(nums[midIndex] <= target and target <= nums[rightIndex]){
                    leftIndex = midIndex + 1;
                } else {
                    rightIndex = midIndex -1;
                }
                
            }
        }
        
        return currentPos;
    }
};