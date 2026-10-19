class Solution {
private:
    std::priority_queue<int> s_nums;
public:
    int findKthLargest(vector<int>& nums, int k) {
        for(int& n : nums){
            s_nums.push(n);
        }
        while(k > 1){
            s_nums.pop();
            k--;
        }
        return s_nums.top();
    }
};
