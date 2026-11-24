class Solution {
public:
    bool isPerfectSquare(int num) {
        long long lp = 1;
        long long rp = num;
        long long mid;
        while (lp <= rp){
            mid = lp + (rp - lp) / 2;
            if (mid * mid < num) {
                lp = mid + 1;
            } else if (mid * mid > num){
                rp = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};