class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> hmap;

        for (int i = 0; i < nums.size(); i++){
            if (hmap.count(target - nums[i])) {
                return {min(i, hmap[target - nums[i]]), 
                        max(i, hmap[target - nums[i]])};
            }
            hmap[nums[i]] = i;
        }

        return {0, 1};
    }
};
