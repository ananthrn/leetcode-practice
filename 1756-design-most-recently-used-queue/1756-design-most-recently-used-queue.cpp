class MRUQueue {
    list<int> Q;
public:
    MRUQueue(int n): Q(0) {
        for(int i = 1; i <= n; i++){
            Q.push_back(i);
        }
    }
    
    int fetch(int k) {
        auto it = next(Q.begin(), k -1);
        int returnVal = *(it);
        Q.erase(it);
        Q.push_back(returnVal);
        
        return returnVal;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */