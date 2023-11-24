#include <stack>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        int n = s.length();
        stk.push(-1);
        int ans = 0;

        for (int i = 0; i<n;i++){
            if (s[i] == '('){
                stk.push(i);
            }else {
                stk.pop();
                if (stk.empty()){
                    stk.push(i);
                }else {
                    ans = max(ans, i - stk.top());
                }
            }
        }

    }
};
