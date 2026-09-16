class Solution {
public:
    bool isValid(string s) {
        // Plan:
        /* use stack
            if open bracket -> push onto stack
            if closed bracket -> check if stack empty or if top matches
            if dont match return false
        */
        stack<char> st;
        unordered_map<char, char> mp {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };
        for (char c : s) {
            if (mp.contains(c)) {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
