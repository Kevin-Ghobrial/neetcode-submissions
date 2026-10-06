class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof {0};
        int min_buy = prices[0];

        for (int sell : prices){
            prof = max(prof, sell - min_buy);
            min_buy = min(min_buy, sell);
        }
        return prof;
    }
};
