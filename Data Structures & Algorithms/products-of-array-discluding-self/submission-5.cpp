class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> res(n);
        std::vector<int> pref(n);
        std::vector<int> suff(n);
        
        // 1, 2, 4, 6
        pref[0] = 1; // [1, 0, 0, 0]
        suff[n - 1] = 1; // [0, 0, 0, 1]
        // [1, (1 * 1), (2 * 1), (4 * 2)]
        // [1, 1, 2, 8]
        for (int i = 1; i < n; i++){
            pref[i] = nums[i - 1] * pref[i - 1];
        }
        // [(2 * 24), (4 * 6), (6 * 1), 1]
        // [48, 24, 6, 1]
        for (int i = n - 2; i >= 0; i--){
            suff[i] = nums[i + 1] * suff[i + 1];
        }
        for (int i = 0; i < n; i++){
            res[i] = pref[i] * suff[i];
        }
        return res;
    }
};
