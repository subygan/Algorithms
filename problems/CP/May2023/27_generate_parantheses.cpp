#include <iostream>
#include <vector>

using namespace std;

void recurse(vector<string> &output, string cur, int n, int open, int close) {


    if (open == n && close == n) return output.push_back(cur);

    if (open < n) recurse(output, cur + '(', n, open + 1, close);

    if (close < open) recurse(output, cur + ')', n, open, close + 1);

}

vector<string> generateParenthesis(int n) {
    vector<string> v;
    recurse(v, "", n, 0, 0);
    return v;
}

int main() {


}

// https://leetcode.com/problems/generate-parentheses
// medium