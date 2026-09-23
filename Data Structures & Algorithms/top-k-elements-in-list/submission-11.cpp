class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int i : nums){
            freq[i]++;
        }
        priority_queue<tuple<int, int>> pq;
        for(const auto& [key, val]: freq){
            pq.push({val, key});
        }
        vector<int> res;
        int rp = pq.size() - 1;
        while (k > 0){
            res.push_back(get<1>(pq.top()));
            pq.pop();
            k--;
        }
        return res;
    }
};
