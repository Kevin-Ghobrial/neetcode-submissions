class Solution {
public:
    int appendCharacters(string s, string t) {
        // pointer for t
        // pointer for s
        // cur target is t's pointer, s moves if target
        // res = len(t) - found from s

        size_t tp = 0;
        size_t sp = 0;
        int count = 0;
        while (tp < t.size() && sp < s.size()){
            if (s[sp] == t[tp]){
                tp++;
                sp++;
                count++;
            } else {
                sp++;
            }
        }

        return t.size() - count;
    }
};