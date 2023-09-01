#include <iostream>
#include <vector>

using namespace std;


void recurse(string& temp, string& digits, vector<string>& sol, vector<string>& m, int idx) {

    if (idx == temp.size() && temp.length()) return sol.push_back(temp);
    int num = digits[idx]-'2';
    string str = m[num];

    for (int i = 0;i<str.length();i++) {
        temp.push_back(str[i]);
        recurse(temp, digits, sol, m, idx+1);
        temp.pop_back();
    }

}


vector<string> letterCombinations(string digits) {

    vector<string> m = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    string temp;
    vector<string> sol;

    recurse(temp, digits, sol, m, 0);
    return sol;
}

int main(){

}

//