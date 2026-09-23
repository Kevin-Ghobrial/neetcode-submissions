class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {  
        unordered_map<string, vector<string>> res;
        for (string s : strs){
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            res[sorted].push_back(s);
        }
        vector<vector<string>> result;
        for (const auto& [key, val] : res){
            result.push_back(val);
        }
        return result;
    }
};
