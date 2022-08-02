class Solution {
public:
    long long findApproxRoot(int num) {
        long long approxRoot = 1;
        while(approxRoot * approxRoot < num){
            approxRoot+=1;
            // approxRoot = (approxRoot + num)/2;
        }
        
        return approxRoot;
    }
    
    long long findApproxRootv2(int num) {
        long l = 1;
        long r = num;
        long currentRoot = 1;
        
        while(l <=r){
            long mid = (l+r)/2;
            if(mid * mid <= num)
            {
                currentRoot = max(mid, currentRoot);
                l = mid+1;
            }
            else if(mid*mid >= num){
                r = mid-1;
            }
        }
        return currentRoot;
    }
    
    bool isPerfectSquare(int num) {
        int val = 1;
        long long approxRoot = findApproxRootv2(num);
        cout<<"approxRoot: "<<approxRoot;
        return (approxRoot * approxRoot) == num;
        
    }
};