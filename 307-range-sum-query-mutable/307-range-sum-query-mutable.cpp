class FenwickTree{
    vector<int> bit;

    int getLower(int index){
        return index & (index + 1);
    }
    
    int getHigher(int index){
        return index | (index + 1);
    }
public:
    FenwickTree(int n): bit(n + 1){
        // bit.resize(n+1, 0);
    }
    
    FenwickTree(const vector<int>& nums): bit(nums.size() + 1){
        int n = nums.size();
        // bit.resize(n+1, 0);
        
        for(int j = 0;  j < nums.size(); j++){
            update(j, nums[j]);
        }
    }
    
    void update(int index, int val){
        while(index < bit.size()){
            bit[index] += val;
            index = getHigher(index);
        }
        
    }
    
    int query(int index){
        int sm = 0; // bit[index];
        
        while(index >=0 ){
            sm += bit[index];
            index = getLower(index) - 1;
            // cout<<"sm, index: "<<sm<<" "<<index<<endl;
        }
        // cout<<endl;
        return sm;
    }
    
    int sumRange(int left, int right){
        int rightRange = query(right);
        int leftRange = (left==0)?0:query(left - 1);
        
        return rightRange - leftRange;
    }
};

class NumArray {
    FenwickTree fTree;
    vector<int> nums;
public:
    NumArray(vector<int>& nums): fTree(nums), nums(nums) {
    }
    
    void update(int index, int val) {
        int currentVal = nums[index];
        nums[index] = val;
        fTree.update(index, val - currentVal);
    }
    
    int sumRange(int left, int right) {
        return fTree.sumRange(left, right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */