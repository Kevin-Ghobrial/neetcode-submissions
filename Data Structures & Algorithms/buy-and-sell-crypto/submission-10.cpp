class Solution {
private:
    int m;
public:
    int maxProfit(vector<int>& prices) {
        int profit {0};
        m = prices[0];
        for (int& i : prices){  
            profit = max(profit, i - m); 
            m = min(m, i);
        }
        return profit;
    }
};
