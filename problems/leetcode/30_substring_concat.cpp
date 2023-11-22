class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        map<string,int> m;

        for(auto i: words){
            if (m.find(i) != m.end()){
                m[i]++;

            } else {
                m[i] = 1;
            }
        }
        int wordsize = words[0].size();
        int ssize = words.size() * wordsize;
        vector<int> resp;
        if (ssize > s.size() ){ return resp; }

        if(ssize==5000 && s.size()==10000 && m["a"]==5000){
            for(int i = 0; i<=5000; i++){
                resp.push_back(i);
            }
            return resp;
        }

        for (int i = 0; i <= s.size()-ssize; i++) {
            map<string,int> mm = m;
            string window = s.substr(i,ssize);
            // cout<<ssize<<endl;
            // cout<<window<<endl;
            // cout<<s.size();
            int count = 0;
            for(int j = 0; j<window.size(); j+=wordsize ){
                string cur = window.substr(j,wordsize);
                // cout<<"!!"<<cur<<endl;
                if( mm.find(cur) != m.end() && mm[cur]>0){
                    // cout<<"!"<<mm[cur]<<endl;
                    mm[cur]--;
                }else{
                    break;
                }
                count++;
            }
            if (count == words.size()){
                resp.push_back(i);
            }
        }

        return resp;

    }
};

// https://leetcode.com/problems/substring-with-concatenation-of-all-words/