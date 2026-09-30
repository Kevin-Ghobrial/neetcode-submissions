class Solution {
public:
    bool isPalindrome(string s) {
        int lp {0};
        int rp = s.size() - 1;
        while (lp < rp) {
            while (lp < rp && !alphaNum(s[rp]) || s[rp] == ' '){
                rp--;
            }
            while (rp > lp && !alphaNum(s[lp]) || s[lp] == ' '){
                lp++;
            }
            if (tolower(s[rp]) != tolower(s[lp])){
                return false;
            }
            rp--;
            lp++;
        }
        return true;
    }


    bool alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
};
