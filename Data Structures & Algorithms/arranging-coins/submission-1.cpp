class Solution {
private:
    std::unordered_map<int, int> cache;
    long long res = 1;
public:
    int arrangeCoins(int n) {
        cache[0] = 1;
        n--;
        int i = 1;
        while (n > 0){
            cache[i] = cache[i - 1] + 1;
            n -= cache[i];
            res++;
            i++;
        }
        if (res == 1) return 1;
        return res - 1;
    }
};