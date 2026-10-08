class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26, 0);
        // basically a counter
        for (char task : tasks) {
            count[task - 'A']++;
            //std::cout << count[task - 'A'] << std::endl;
        }
        priority_queue<int> maxHeap;
        for (int& c : count) {
            if (c > 0){
                maxHeap.push(c);
            }
        }

        int time {0};
        queue<pair<int, int>> q;
        while (!maxHeap.empty() || !q.empty()) {
            time++;

            if (maxHeap.empty()) {
                time = q.front().second;
            } else {
                int c = maxHeap.top() - 1;
                maxHeap.pop();
                if (c > 0) {
                    q.push({c, time + n});
                }
            }

            if (!q.empty() && q.front().second == time){
                maxHeap.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};
