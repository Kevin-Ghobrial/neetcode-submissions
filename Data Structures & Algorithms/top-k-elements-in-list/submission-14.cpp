class Solution {
private:
    std::unordered_map<int, int> freq;
    std::priority_queue<std::tuple<int, int>> tops;
    std::vector<int> res;
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        for (int& i : nums){
            freq[i] += 1;
        }   
        for (auto& [key, val] : freq){
            tops.push({val, key});
        }
        
        while (k > 0){
            auto& [val, key] = tops.top();
            res.push_back(key);
            tops.pop();
            k--;
        }
        return res;
    }
};
