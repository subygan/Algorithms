#include <iostream>

using namespace std;

int strStr(string haystack, string needle) {
    char ni = needle[0];

    int diff = haystack.length() - needle.length();

    for (int i = 0; i < diff+1; i++) {
        if (haystack[i] == ni) {
            for (int j = 0; j < needle.length(); j++){
                if (haystack[i+j] != needle[j]){
                    break;
                }
                if (j == needle.length()-1){
                    return i;
                }
            }
        }
    }
    return -1;
}


int main(){
    cout<<strStr("123a","a")<<endl;
}

// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
// #easy