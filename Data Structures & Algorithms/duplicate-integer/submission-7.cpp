class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dup;
        for (int n : nums){
            if (dup.count(n)){
                return true;
            }
            dup.insert(n);
        }
        return false;
    }
};