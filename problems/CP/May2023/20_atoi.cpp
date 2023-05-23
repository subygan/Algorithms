#include <iostream>
#include <vector>

using namespace std;


int myAtoi(string s) {

    double num = 0;
    int i = 0;
    while(s[i] == ' ') i++;
    cout<<i<<endl;
    cout<<s<<endl;
    if (s[i]!='+' && s[i]!='-') s.insert(i,"+");
    cout<<s<<endl;
    int len = s.size();
    int neg = ','-s[i++];
    cout<<i<<" "<<len<<endl;

    while(i < len && s[i] >= '0' && s[i] <= '9'){
        num = num*10 + (s[i]-'0');
        i++;
    }
    cout<<num<<endl;
    num = num*neg;

    num = (num > INT_MAX) ? INT_MAX : num;
    num = (num < INT_MIN) ? INT_MIN : num;

    return int(num);
}


int main() {
    cout<<myAtoi(" +0000000000012345678");

}
