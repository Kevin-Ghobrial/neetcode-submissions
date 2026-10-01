class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::set<int> visited;
        for (auto i : nums){
            if (visited.contains(i)){
                return i;
            }
            visited.insert(i);
        }
        return 0;
    }
};
