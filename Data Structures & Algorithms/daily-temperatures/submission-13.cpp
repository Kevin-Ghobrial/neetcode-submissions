class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res(temperatures.size(), 0);
        std::stack<int> waiting;

        for (int i {0}; i < static_cast<int>(temperatures.size()); ++i){
            while (!waiting.empty() && temperatures[i] > temperatures[waiting.top()]){     
                int prev = waiting.top();
                waiting.pop();
                res[prev] = i - prev;
            }
            waiting.push(i);
        }
        return res;
    }
};
