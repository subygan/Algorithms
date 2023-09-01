#include <iostream>
#include <vector>
#include <string>

using namespace std;


bool count(vector<int> val, int pos, int red, int blue) {

    if (pos >= val.size()) {
        return red%2 == blue%2;
    }

    return count(val, pos + 1, red + val[pos], blue) || count(val, pos + 1, red, blue + val[pos]);
}

int main() {

    int tests;
    cin >> tests;

    for (int i = 0; i < tests; i++) {
        int nums;

        vector<int> val;
        cin >> nums;
        int num;
        for (int i=0;i<nums;i++) {

            cin>>num;
            val.push_back(num);

//            int c = i - '0';
//            cout<<c<<endl;
//            if (c > 0 && c < 10) {
//                num = num * 10 + c;
//                continue;
//            }
//            val.push_back(num);
//            nums = 0;
        }

//        for(auto z: val){cout<<z<<" ";}

        if (count(val, 0, 0, 0)) {
            cout << "YES"<<endl;
        } else { cout << "NO"<<endl; }
    }

//    vector<int> v = {4,7};
//    cout<<count(v,0,0,0)<<endl;
//    return 0;
}