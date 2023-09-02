class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()){
            return false;
        }
        vector<int> vs =  vector(26,0);
        vector<int> vt =  vector(26,0);
        for(int i = 0; i< s.size(); i++) {
            int cs  = s[i] - 'a';
            vs[cs]++;
            int ct  =  t[i] - 'a';
            vt[ct]++;
        }

        for(int j = 0; j<26; j++){
            if (vs[j]!=vt[j]){return false;}
        }
        return true;

    }
};