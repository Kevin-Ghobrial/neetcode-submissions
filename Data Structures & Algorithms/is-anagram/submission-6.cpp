class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }

        int len = s.size();

        unordered_map <char, int> s_map;
        unordered_map <char, int> t_map;

        for(int i = 0; i < len; i++){
            s_map[s[i]]++;
            t_map[t[i]]++;
        }
        
        bool isAna = s_map == t_map ? true : false;
        
        return isAna;
    }
};
