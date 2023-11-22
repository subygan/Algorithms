#include <stdio.h>
#include <string>
using namespace std;

bool isMatch(string s, string p){

    char prev;

    for (int i = 0; i < s.size(); i++){
        string pat = p;
        for (int j = i; j < p.size(); j++){
            if (pat[j] == '.'){
                prev = pat[j];
                continue;
            }
            if (pat[j] == '*'){
                if (prev == s[i]){
                    continue;
                }
                else{
                    break;
                }
            }


        }
    }


}

int main(){


}