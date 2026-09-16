class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq; // key (number) -> val (freq)
        for (int n : nums) {
            freq[n]++;
        }
        vector<pair<int, int>> res;
        for (const auto& [key, value] : freq){
            res.push_back({value, key});
        }
        sort(res.begin(), res.end());
        
        vector<int> final;
        for (int i = res.size() - 1; i >= (int)res.size() - k; i--){
            final.push_back(res[i].second);
        }
        return final;
    }
};
