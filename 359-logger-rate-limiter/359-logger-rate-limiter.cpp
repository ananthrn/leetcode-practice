class Logger {
private:
    unordered_map<string, int> logTime;
public:
    Logger() {
        logTime = {};
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if(logTime.count(message) == 0 or logTime[message]<= timestamp - 10){
            logTime[message] = timestamp;
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */