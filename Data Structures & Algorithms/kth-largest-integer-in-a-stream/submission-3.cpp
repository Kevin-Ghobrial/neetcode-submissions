class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int& n : nums){
            this->minHeap.push(n);
            if (this->minHeap.size() > k){
                this->minHeap.pop();
            }
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > k){
            minHeap.pop();
        }   
        return minHeap.top(); 
    }


};
