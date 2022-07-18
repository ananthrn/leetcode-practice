class Solution {
public:
    int getKth(int lo, int hi, int k) {
        auto power = [](int x){
            int steps = 0;
            
            while(x > 1){
                x = (x%2 == 0)?x/2: 3* x + 1;
                steps+=1;
            }
            
            return steps;
        };
        
        auto comp = [power](const int& a, const int& b){
            int pow_a  = power(a), pow_b = power(b);
            
            return (pow_a == pow_b)? a < b: pow_a < pow_b;
        };
        
        vector<int> vals;
        
        for(int j = lo; j <= hi; j++){
            vals.push_back(j);
        }
        
        sort(vals.begin(), vals.end(), comp);
        
        return vals[k-1];
    }
};