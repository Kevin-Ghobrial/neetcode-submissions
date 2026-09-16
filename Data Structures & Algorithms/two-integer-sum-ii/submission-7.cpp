class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // sort
        sort(numbers.begin(), numbers.end());

        int lp = 0;
        int rp = numbers.size() - 1;
        while (lp < rp){
            if (numbers[lp] + numbers[rp] == target) {
                return {lp + 1, rp + 1};
            } 
            else if (numbers[lp] + numbers[rp] > target) {
                rp--;
            }
            else {
                lp++;
            }
        }
        return {};
    }
};
