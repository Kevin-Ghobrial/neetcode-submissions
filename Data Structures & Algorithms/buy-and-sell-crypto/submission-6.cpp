using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof = 0;
        int minBuy = prices[0];

        for(int& sell : prices) {
            prof = max(prof, sell - minBuy);
            minBuy = min(minBuy, sell);
        }

        return prof;
    }
};
