class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num == 1) return true;
        int i = 0;
        while (i < num){
            if (i * i == num) return true;
            i++;
        }
        return false;
    }
};