class Solution {
private:  
    std::unordered_map<int, int> freqs; 
public:
    // priority_queue -> pair{freq, val}

    vector<int> topKFrequent(vector<int>& nums, int k) {
        for (const auto& n : nums){
            freqs[n]++;
        }
        std::vector<std::pair<int, int>> res;
        for (const auto& [key, val] : freqs){
            res.push_back({key, val});
        }

        std::sort(res.begin(), res.end(),
        [](const auto& a, const auto& b){
            return a.second > b.second;
        });

        std::vector<int> final_res;
        int len = std::min(static_cast<size_t>(k), res.size());
        for (size_t i = 0; i < len; i++){
            final_res.push_back(res[i].first);
        }

        return final_res;
    }
};
