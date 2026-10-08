class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // key: number, value: frequency
        std::unordered_map<int, int> freq;
        for (int& n : nums){
            freq[n] += 1;
        }

        std::vector<pair<int, int>> values(freq.begin(), freq.end());

        std::sort(values.begin(), values.end(), 
                    [](const auto& a, const auto& b){
                        return a.second > b.second;
                    });

        std::vector<int> res;
        int i {0};
        while (k){
            res.push_back(values[i].first);
            k--;
            i++;
        }
        return res;
    }
};
