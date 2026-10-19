class KthLargest {
private:
    int k;
    std::vector<int> nums;
    std::priority_queue<int> s_nums;
public:
    KthLargest(int k, vector<int>& nums) 
        : k(k), nums(nums)
    {
        for (int& i : nums){
            s_nums.push(i);
        }
    }
    
    int add(int val) {
        s_nums.push(val);
        auto copy_s_nums = s_nums;
        int i = k;
        // 3, 3, 3, 2, 1
        while(i > 1){
            copy_s_nums.pop();
            i--;
        }

        return copy_s_nums.top();
    }
};
