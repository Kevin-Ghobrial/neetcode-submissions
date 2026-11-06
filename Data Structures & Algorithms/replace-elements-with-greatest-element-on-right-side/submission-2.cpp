class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        if(arr.size() == 1){
            arr[0] = -1;
            return arr;
        }
        if (arr.size() <= 2){
            arr[0] = std::max(arr[0], arr[1]);
            arr[1] = -1;
            return arr;
        }
        int curMax = arr[arr.size() - 1];
        int i = arr.size() - 2;
        while (i >= 0){
            int nextMax = std::max(curMax, arr[i]);
            arr[i] = curMax;
            curMax = nextMax;
            i--;
        }
        arr[arr.size() - 1] = -1;

        return arr;
    }
};