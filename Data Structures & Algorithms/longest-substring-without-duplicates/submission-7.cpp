class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> visited;
        int count = 0;
        int lp = 0;

        for (char& c : s){
            while (visited.contains(c)){
                visited.erase(s[lp]);
                lp++;
            }
            visited.insert(c);
            count = std::max(std::size_t(count), visited.size());
        }
        return count;
    }
};
