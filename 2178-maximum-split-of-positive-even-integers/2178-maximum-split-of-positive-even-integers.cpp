class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        if(finalSum %2){
            return {};
        }
        long long currentVal = 2;
        long long currentSum = 0;
        vector<long long> comps;
        
        while(currentSum + currentVal <= finalSum){
            comps.push_back(currentVal);
            currentSum += currentVal;
            currentVal += 2;
        }
        
        comps.back() += finalSum - currentSum;
        
        return comps;
    }
};