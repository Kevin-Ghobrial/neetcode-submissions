class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {  
        unordered_map<string, vector<string>> anas;

        for (string s : strs){
            string key = s;
            sort(key.begin(), key.end());
            anas[key].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& [key, value] : anas) {
            res.push_back(value);
        }   

        return res;
    }
};
