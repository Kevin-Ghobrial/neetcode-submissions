class Solution {
public:
    int arrangeCoins(int n) {
        return floor(-.5 + sqrt((double)2*n+.25));
    }
};