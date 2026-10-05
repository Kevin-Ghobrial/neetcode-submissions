class Solution {
public:
    int search(vector<int>& nums, int target) {
        long lp = 0, rp = nums.size() - 1;
        while (lp <= rp){
            long mid = (lp + (rp - lp / 2));
            std::cout << mid << '\n';
            if (nums[mid] < target){
                lp = ++mid;
                
            } else if (nums[mid] > target){
                rp = --mid;
                
            } else {
                return mid;
            }
        }
        return -1;
    }
};
