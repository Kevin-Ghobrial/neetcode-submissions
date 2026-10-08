class Solution {
private:
    std::priority_queue<int> maxHeap;

public:
    int lastStoneWeight(vector<int>& stones) {
        for (int& s : stones){
            maxHeap.push(s);
        }
        while(maxHeap.size() > 1){
            int a = (maxHeap.top());
            maxHeap.pop();
            int b = (maxHeap.top());
            maxHeap.pop();
        
            if (a == b){
                continue;
            } else if (a < b){
                maxHeap.push((b - a));
            } else{
                maxHeap.push((a - b));
            }
        }
        if (maxHeap.size() > 0){
            return maxHeap.top();
        }
        return 0;
    }
};
