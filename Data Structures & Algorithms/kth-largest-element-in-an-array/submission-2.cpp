class Solution {
private:
    std::priority_queue<int> maxHeap;
public:
    int findKthLargest(vector<int>& nums, int k) {
        for (int& n : nums){
            maxHeap.push(n);
        }
        int target_len = nums.size() - k;
        while (maxHeap.size() > target_len + 1){
            maxHeap.pop();
        }

        return maxHeap.top();
    }
};
