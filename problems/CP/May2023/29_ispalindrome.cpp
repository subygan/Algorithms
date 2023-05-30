#include <iostream>
#include <vector>

using namespace std;


bool isPalindrome(string s) {


    int n = s.length();
    int i = 0;
    string m;
    while (i < n) {
        int c = ::tolower(s[i]) - 'a';
        if (c >= 0 && c <= 25) {
            m.push_back(tolower(s[i++]));
            continue;
        }
        i++;
    }
//    cout << m<<endl;
    i = 0;
    n = m.length()-1;
//    cout <<n<<endl;
    while (i <= n) {
//        cout<<i<<" "<<n<<" "<<m[m.length()]<<endl;
//        cout << m[i]<<" "<< m[n]<<endl;
        if (m[i++] != m[n--]) return false;

    }

    return true;
}

int main() {

    cout<<isPalindrome("A man, a plan, a canal: Panama");

}

// https://leetcode.com/problems/valid-palindrome/
// easy